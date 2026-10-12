
import pandas as pd
from pathlib import Path

# Define paths
BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / "data" / "raw"
REPORT_DIR = BASE_DIR / "reports"

REPORT_DIR.mkdir(exist_ok=True)

# Load datasets
fund_master = pd.read_csv(RAW_DIR / "01_fund_master.csv")
nav_history = pd.read_csv(RAW_DIR / "02_nav_history.csv")

print("=" * 60)
print("AMFI SCHEME CODE VALIDATION")
print("=" * 60)

# Normalize scheme codes for comparison
def normalize_codes(series):
    return series.astype("string").str.strip().str.replace(
        r"\.0$", "", regex=True
    )

fund_master["amfi_code"] = normalize_codes(fund_master["amfi_code"])
nav_history["amfi_code"] = normalize_codes(nav_history["amfi_code"])

# Remove missing and blank codes from comparison
master_codes = set(
    fund_master["amfi_code"].dropna().loc[
        lambda s: s.ne("")
    ]
)

nav_codes = set(
    nav_history["amfi_code"].dropna().loc[
        lambda s: s.ne("")
    ]
)

# Compare codes
matching_codes = master_codes.intersection(nav_codes)
missing_codes = master_codes.difference(nav_codes)
extra_codes = nav_codes.difference(master_codes)

# Check null and duplicate codes
master_nulls = fund_master["amfi_code"].isna().sum()
nav_nulls = nav_history["amfi_code"].isna().sum()

master_duplicates = fund_master["amfi_code"].dropna().duplicated().sum()
nav_duplicate_rows = nav_history.duplicated(
    subset=["amfi_code", "date"]
).sum()

# Display results
print(f"\nTotal Fund Master Records: {len(fund_master)}")
print(f"Total NAV History Records: {len(nav_history)}")

print(f"\nUnique Fund Master Codes: {len(master_codes)}")
print(f"Unique NAV History Codes: {len(nav_codes)}")

print(f"\nMatching AMFI Codes: {len(matching_codes)}")
print(f"Missing Codes in NAV History: {len(missing_codes)}")
print(f"Extra Codes in NAV History: {len(extra_codes)}")

print(f"\nNull Fund Master Codes: {master_nulls}")
print(f"Null NAV History Codes: {nav_nulls}")
print(f"Duplicate Fund Master Codes: {master_duplicates}")
print(f"Duplicate NAV Scheme-Date Records: {nav_duplicate_rows}")

# Calculate validation percentage
validation_pct = (
    len(matching_codes) / len(master_codes) * 100
    if master_codes else 0
)

print(f"\nAMFI Code Coverage: {validation_pct:.2f}%")

# Save missing codes
missing_df = fund_master[
    fund_master["amfi_code"].isin(missing_codes)
]

missing_df.to_csv(
    REPORT_DIR / "missing_amfi_codes.csv",
    index=False
)

# Save validation summary
summary = pd.DataFrame([{
    "fund_master_records": len(fund_master),
    "nav_history_records": len(nav_history),
    "unique_master_codes": len(master_codes),
    "unique_nav_codes": len(nav_codes),
    "matching_codes": len(matching_codes),
    "missing_codes": len(missing_codes),
    "extra_nav_codes": len(extra_codes),
    "master_null_codes": int(master_nulls),
    "nav_null_codes": int(nav_nulls),
    "master_duplicate_codes": int(master_duplicates),
    "duplicate_nav_scheme_dates": int(nav_duplicate_rows),
    "coverage_percentage": round(validation_pct, 2)
}])

summary.to_csv(
    REPORT_DIR / "amfi_validation_summary.csv",
    index=False
)

print("\nValidation reports saved successfully!")

if not missing_codes and master_nulls == 0:
    print("RESULT: PASS - All Fund Master AMFI codes exist in NAV History.")
else:
    print("RESULT: REVIEW REQUIRED - Missing or null AMFI codes detected.")
