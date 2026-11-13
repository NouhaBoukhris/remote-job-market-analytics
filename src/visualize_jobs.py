"""Create reproducible charts and a skills-frequency table from the cleaned snapshot."""
import argparse
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

def bar(series, title, xlabel, path):
    fig, ax = plt.subplots(figsize=(10, 6))
    series.plot.bar(ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Number of job listings")
    ax.tick_params(axis="x", rotation=40)
    fig.tight_layout()
    fig.savefig(path, dpi=160)
    plt.close(fig)

def visualize(source: Path, charts: Path, skills_output: Path) -> None:
    df = pd.read_csv(source, encoding="utf-8-sig")
    charts.mkdir(parents=True, exist_ok=True)
    skills_output.parent.mkdir(parents=True, exist_ok=True)
    bar(df["company"].value_counts().head(10), "Top companies in snapshot", "Company", charts / "top_companies.png")
    bar(df["location"].value_counts().head(10), "Reported locations", "Location", charts / "top_locations.png")
    tags = df["skills"].fillna("").str.split(",").explode().str.strip()
    counts = tags[tags.ne("") & tags.notna()].value_counts().head(15)
    bar(counts, "Most frequent listing tags", "Tag", charts / "top_skills.png")
    counts.rename_axis("skill").reset_index(name="frequency").to_csv(skills_output, index=False)
    fig, ax = plt.subplots(figsize=(9, 5))
    df["number_of_skills"].dropna().plot.hist(bins=10, ax=ax)
    ax.set_title("Number of tags per job listing")
    ax.set_xlabel("Tags per listing")
    fig.tight_layout()
    fig.savefig(charts / "skills_distribution.png", dpi=160)
    plt.close(fig)
    dates = pd.to_datetime(df["date_posted"], errors="coerce", utc=True)
    daily = dates.dropna().dt.date.value_counts().sort_index()
    if not daily.empty:
        fig, ax = plt.subplots(figsize=(10, 5))
        daily.plot(ax=ax, marker="o")
        ax.set_title("Listings by posting date in snapshot")
        ax.set_xlabel("Posting date")
        ax.set_ylabel("Listings")
        fig.tight_layout()
        fig.savefig(charts / "jobs_over_time.png", dpi=160)
        plt.close(fig)
    print(f"Charts saved to {charts}; skills table saved to {skills_output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=Path("data/jobs_final_cleaned.csv"))
    parser.add_argument("--charts", type=Path, default=Path("images/charts"))
    parser.add_argument("--skills-output", type=Path, default=Path("data/skills_frequency.csv"))
    args = parser.parse_args()
    visualize(args.input, args.charts, args.skills_output)
