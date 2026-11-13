"""Clean a Remote OK snapshot without inventing missing values or salary units."""
import argparse
from pathlib import Path
import pandas as pd

REQUIRED = {"url", "title", "company", "location", "date_posted", "skills"}

def clean(source: Path, output: Path) -> None:
    df = pd.read_csv(source, encoding="utf-8-sig")
    missing = REQUIRED - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    df = df.copy()
    for col in ("url", "title", "company", "location", "skills"):
        df[col] = df[col].astype("string").str.strip()
    # Preserve records only when both title and company are available.
    df = df.dropna(subset=["title", "company"])
    df = df[(df["title"] != "") & (df["company"] != "")]
    df = df[~df["title"].str.fullmatch(r"(?i)test job", na=False)]
    df = df.drop_duplicates(subset=["url"], keep="first")
    df["location"] = df["location"].fillna("Remote").replace("", "Remote")
    df["date_posted"] = pd.to_datetime(df["date_posted"], errors="coerce", utc=True)
    df["skills"] = df["skills"].fillna("").str.lower()
    df["number_of_skills"] = df["skills"].apply(
        lambda s: len([tag for tag in s.split(",") if tag.strip()])
    )
    # Do not derive salary midpoints from unvalidated free-text salary fields.
    # Some location strings in the original snapshot have encoding artifacts;
    # these are not silently rewritten without checking the source.
    output.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output, index=False, encoding="utf-8-sig")
    print(f"Saved {len(df)} cleaned listings to {output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=Path("data/jobs_data.csv"))
    parser.add_argument("--output", type=Path, default=Path("data/jobs_final_cleaned.csv"))
    args = parser.parse_args()
    clean(args.input, args.output)
