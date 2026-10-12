
import pandas as pd
from pathlib import Path

# Load fund master dataset
file_path = Path("data/raw/01_fund_master.csv")
df = pd.read_csv(file_path)

print("=" * 60)
print("FUND MASTER EXPLORATION")
print("=" * 60)

# Display dataset information
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Records:")
print(df.head().to_string(index=False))

# Identify columns using common naming variations
def find_column(keywords):
    for col in df.columns:
        normalized = col.lower().replace("_", " ").strip()
        if any(keyword in normalized for keyword in keywords):
            return col
    return None

columns_to_explore = {
    "Fund Houses": ["fund house", "amc"],
    "Categories": ["category"],
    "Sub-Categories": ["sub category", "subcategory"],
    "Risk Grades": ["risk grade", "risk level", "riskometer"],
    "AMFI Scheme Codes": ["amfi code", "scheme code"]
}

for label, keywords in columns_to_explore.items():
    col = find_column(keywords)

    print(f"\n{'=' * 50}")
    print(label.upper())
    print("=" * 50)

    if col:
        print(f"Column: {col}")
        print(f"Unique values: {df[col].nunique()}")
        print(df[col].value_counts(dropna=False).to_string())
    else:
        print("Column not automatically identified.")

print("\nFund master exploration completed!")
