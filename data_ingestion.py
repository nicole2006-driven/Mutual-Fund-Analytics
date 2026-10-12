
import pandas as pd
from pathlib import Path

# Path to the raw datasets
DATA_DIR = Path(__file__).resolve().parent / "data" / "raw"

# Find all CSV files
csv_files = sorted(DATA_DIR.glob("[0-9][0-9]_*.csv"))

print("=" * 60)
print("MUTUAL FUND DATA INGESTION")
print("=" * 60)

print(f"\nTotal CSV datasets found: {len(csv_files)}")

if len(csv_files) != 10:
    print("WARNING: Expected 10 CSV datasets.")

summary = []

for file in csv_files:
    print("\n" + "=" * 60)
    print(f"DATASET: {file.name}")
    print("=" * 60)

    try:
        df = pd.read_csv(file, low_memory=False)

        # Dataset shape
        print("\n1. Shape (Rows, Columns):")
        print(df.shape)

        # Column data types
        print("\n2. Data Types:")
        print(df.dtypes)

        # First five rows
        print("\n3. First 5 Rows:")
        print(df.head().to_string(index=False))

        # Missing values
        print("\n4. Missing Values:")
        print(df.isnull().sum().to_string())

        # Duplicate rows
        duplicates = df.duplicated().sum()
        print(f"\n5. Duplicate Rows: {duplicates}")

        # Summary
        summary.append({
            "Dataset": file.name,
            "Rows": df.shape[0],
            "Columns": df.shape[1],
            "Missing Values": int(df.isnull().sum().sum()),
            "Duplicate Rows": int(duplicates)
        })

    except Exception as e:
        print(f"ERROR loading {file.name}: {e}")

# Final summary
summary_df = pd.DataFrame(summary)

print("\n" + "=" * 60)
print("FINAL DATA QUALITY SUMMARY")
print("=" * 60)
print(summary_df.to_string(index=False))

# Save report
REPORT_DIR = Path(__file__).resolve().parent / "reports"
REPORT_DIR.mkdir(exist_ok=True)

summary_df.to_csv(
    REPORT_DIR / "data_quality_summary.csv",
    index=False
)

print("\nData quality summary saved successfully!")
