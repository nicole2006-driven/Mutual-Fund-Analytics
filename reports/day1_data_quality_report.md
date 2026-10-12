# Day 1 — Mutual Fund Data Quality Report

## Objective
To validate the consistency, completeness, and integrity of AMFI scheme codes across the Fund Master and NAV History datasets.

## Dataset Overview
- Fund Master: 40 records
- NAV History: 46,000 records
- Unique mutual fund schemes: 40

## Validation Results
- All 40 AMFI scheme codes in the Fund Master are present in NAV History.
- No missing or extra AMFI scheme codes were identified.
- No null AMFI codes were found.
- No duplicate AMFI codes were found in the Fund Master.
- No duplicate scheme-date combinations were identified in NAV History.
- AMFI scheme code coverage: **100%**

## Data Quality Observations
The Fund Master and NAV History datasets demonstrate complete referential coverage for AMFI scheme codes. The validation did not identify any missing scheme references or duplicate scheme-date records.

Other potential data quality issues, such as missing NAV values, invalid dates, or inconsistent numerical values, require separate validation.

## Conclusion
**Status: PASS**

All 40 mutual fund schemes have corresponding NAV history records. The AMFI code validation requirement for Day 1 has been successfully fulfilled.