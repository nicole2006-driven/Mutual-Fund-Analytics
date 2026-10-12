
import requests
import pandas as pd
from pathlib import Path

BASE_URL = "https://api.mfapi.in/mf"

RAW_DIR = Path(__file__).resolve().parent / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

# Scheme codes provided in the assignment
schemes = {
    "HDFC_Top_100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

all_latest_nav = []

for scheme_name, scheme_code in schemes.items():
    print(f"\nFetching NAV for {scheme_name} ({scheme_code})...")

    try:
        url = f"{BASE_URL}/{scheme_code}"
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        result = response.json()

        nav_history = result.get("data", [])
        meta = result.get("meta", {})

        if not nav_history:
            print(f"No NAV data available for {scheme_name}")
            continue

        # Save the complete NAV history for this scheme
        df = pd.DataFrame(nav_history)
        df["scheme_code"] = scheme_code
        df["scheme_name"] = meta.get("scheme_name", scheme_name)

        filename = RAW_DIR / f"api_{scheme_name}.csv"
        df.to_csv(filename, index=False)

        print(f"Saved: {filename.name}")
        print(f"Total NAV records: {len(df)}")

        # Extract latest available NAV
        latest = nav_history[0]

        all_latest_nav.append({
            "scheme_code": scheme_code,
            "scheme_name": meta.get("scheme_name", scheme_name),
            "nav_date": latest.get("date"),
            "nav": latest.get("nav")
        })

        print(f"Latest available NAV: {latest.get('nav')}")
        print(f"NAV Date: {latest.get('date')}")

    except requests.RequestException as e:
        print(f"API request failed: {e}")
    except (ValueError, TypeError) as e:
        print(f"Invalid API response: {e}")

# Save combined latest NAV summary
if all_latest_nav:
    summary_df = pd.DataFrame(all_latest_nav)

    output = RAW_DIR / "api_latest_nav_summary.csv"
    summary_df.to_csv(output, index=False)

    print("\n" + "=" * 60)
    print("LATEST NAV SUMMARY")
    print("=" * 60)
    print(summary_df.to_string(index=False))
    print(f"\nSaved: {output}")
else:
    print("\nNo NAV records were retrieved.")
