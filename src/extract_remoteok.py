"""Collect a dated snapshot of remote job listings from the Remote OK JSON API."""
import argparse
from datetime import datetime, timezone
from pathlib import Path
import pandas as pd
import requests

API_URL = "https://remoteok.com/api"

def extract(output: Path) -> None:
    response = requests.get(API_URL, headers={"User-Agent": "RemoteJobMarketAnalytics/1.0 (educational research)"}, timeout=30)
    response.raise_for_status()
    payload = response.json()
    if not isinstance(payload, list):
        raise ValueError("Expected a list from Remote OK API")
    jobs = []
    for item in payload:
        if not isinstance(item, dict) or not item.get("position"):
            continue  # API can include a metadata entry
        tags = item.get("tags") or []
        jobs.append({
            "url": item.get("url"), "title": item.get("position"),
            "company": item.get("company"), "location": item.get("location") or "Remote",
            "remote": True, "job_type": "Remote", "salary": item.get("salary"),
            "date_posted": item.get("date"), "skills": ", ".join(map(str, tags)),
        })
    if not jobs:
        raise ValueError("API returned no job listings; no output written")
    output.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(jobs).to_csv(output, index=False, encoding="utf-8-sig")
    print(f"Saved {len(jobs)} listings to {output} at {datetime.now(timezone.utc).isoformat()}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("data/jobs_data.csv"))
    args = parser.parse_args()
    extract(args.output)
