#!/usr/bin/env python3
"""
Extract data from Excel/CSV/JSON files and output standardized JSON for charting.

Usage:
    python3 extract_data.py <file_path> [--sheet <name>] [--limit <rows>] [--preview]

Output JSON format:
{
    "sheets": [
        {
            "name": "Sheet1",
            "headers": ["col1", "col2", ...],
            "rows": [{"col1": val1, "col2": val2}, ...],
            "dtypes": {"col1": "string", "col2": "number", ...},
            "stats": {"col2": {"min": 0, "max": 100, "mean": 50}, ...},
            "row_count": 100
        }
    ],
    "summary": "Brief description of the data"
}
"""

import argparse
import json
import sys
import os
from pathlib import Path


def detect_file_type(file_path: str) -> str:
    ext = Path(file_path).suffix.lower()
    type_map = {
        ".xlsx": "excel", ".xls": "excel", ".xlsm": "excel",
        ".csv": "csv", ".tsv": "tsv",
        ".json": "json", ".jsonl": "jsonl",
    }
    return type_map.get(ext, "unknown")


def read_excel(file_path: str, sheet_name=None) -> list:
    try:
        import openpyxl
    except ImportError:
        print("Installing openpyxl...", file=sys.stderr)
        os.system(f"{sys.executable} -m pip install openpyxl -q")
        import openpyxl

    import pandas as pd
    xls = pd.ExcelFile(file_path, engine="openpyxl")
    sheets_to_read = [sheet_name] if sheet_name else xls.sheet_names
    results = []
    for sn in sheets_to_read:
        df = pd.read_excel(xls, sheet_name=sn)
        results.append(df_to_sheet(df, sn))
    return results


def read_csv(file_path: str, sep=",") -> list:
    import pandas as pd
    df = pd.read_csv(file_path, sep=sep)
    return [df_to_sheet(df, Path(file_path).stem)]


def read_json(file_path: str) -> list:
    import pandas as pd
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        df = pd.DataFrame(data)
        return [df_to_sheet(df, Path(file_path).stem)]
    elif isinstance(data, dict):
        results = []
        for key, val in data.items():
            if isinstance(val, list):
                df = pd.DataFrame(val)
                results.append(df_to_sheet(df, key))
        if not results:
            df = pd.DataFrame([data])
            results.append(df_to_sheet(df, Path(file_path).stem))
        return results
    return []


def read_jsonl(file_path: str) -> list:
    import pandas as pd
    records = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    df = pd.DataFrame(records)
    return [df_to_sheet(df, Path(file_path).stem)]


def df_to_sheet(df, name: str) -> dict:
    import pandas as pd
    import numpy as np

    # Clean column names
    df.columns = [str(c).strip() for c in df.columns]

    # Detect types
    dtypes = {}
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            dtypes[col] = "number"
        elif pd.api.types.is_datetime64_any_dtype(df[col]):
            dtypes[col] = "date"
        else:
            # Try parsing as date
            try:
                pd.to_datetime(df[col], errors="raise")
                dtypes[col] = "date"
            except (ValueError, TypeError):
                dtypes[col] = "string"

    # Compute stats for numeric columns
    stats = {}
    for col, dtype in dtypes.items():
        if dtype == "number":
            series = df[col].dropna()
            if len(series) > 0:
                stats[col] = {
                    "min": float(series.min()),
                    "max": float(series.max()),
                    "mean": round(float(series.mean()), 2),
                    "sum": float(series.sum()),
                }

    # Convert rows, handle NaN and special types
    def clean_value(v):
        if isinstance(v, float) and (np.isnan(v) or np.isinf(v)):
            return None
        if isinstance(v, (np.integer,)):
            return int(v)
        if isinstance(v, (np.floating,)):
            return float(v)
        if isinstance(v, pd.Timestamp):
            return v.isoformat()
        return v

    rows = []
    for _, row in df.iterrows():
        rows.append({col: clean_value(row[col]) for col in df.columns})

    return {
        "name": name,
        "headers": list(df.columns),
        "rows": rows,
        "dtypes": dtypes,
        "stats": stats,
        "row_count": len(df),
    }


def generate_summary(sheets: list) -> str:
    parts = []
    for s in sheets:
        num_cols = [c for c, t in s["dtypes"].items() if t == "number"]
        str_cols = [c for c, t in s["dtypes"].items() if t == "string"]
        date_cols = [c for c, t in s["dtypes"].items() if t == "date"]
        parts.append(
            f"Sheet '{s['name']}': {s['row_count']} rows, "
            f"{len(s['headers'])} columns "
            f"({len(num_cols)} numeric, {len(str_cols)} text, {len(date_cols)} date)"
        )
    return "; ".join(parts)


def main():
    parser = argparse.ArgumentParser(description="Extract data for dashboard visualization")
    parser.add_argument("file_path", help="Path to data file (Excel/CSV/JSON)")
    parser.add_argument("--sheet", help="Specific sheet name (Excel only)")
    parser.add_argument("--limit", type=int, default=0, help="Limit rows (0=all)")
    parser.add_argument("--preview", action="store_true", help="Show first 5 rows only")
    args = parser.parse_args()

    file_type = detect_file_type(args.file_path)

    readers = {
        "excel": lambda: read_excel(args.file_path, args.sheet),
        "csv": lambda: read_csv(args.file_path),
        "tsv": lambda: read_csv(args.file_path, sep="\t"),
        "json": lambda: read_json(args.file_path),
        "jsonl": lambda: read_jsonl(args.file_path),
    }

    if file_type not in readers:
        print(json.dumps({"error": f"Unsupported file type: {Path(args.file_path).suffix}"}))
        sys.exit(1)

    sheets = readers[file_type]()

    # Apply limits
    limit = 5 if args.preview else args.limit
    if limit > 0:
        for s in sheets:
            s["rows"] = s["rows"][:limit]
            s["row_count_original"] = s["row_count"]
            s["row_count"] = len(s["rows"])

    output = {
        "sheets": sheets,
        "summary": generate_summary(sheets),
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
