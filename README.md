# Remote Job Market Analytics | Python & Power BI

**API data extraction · Data cleaning · Exploratory analysis · Power BI**

An academic project exploring remote-job listings, reported locations, employers, and recurring skill tags. Data was obtained from the [Remote OK API](https://remoteok.com/api), rather than by scraping website HTML.

> **Portfolio status:** Reorganized Python scripts are available. Original datasets are imported; the Power BI dashboard, report and presentation are still to be migrated from the [original coursework repository](https://github.com/nouhaBks/Website-Scarper). The revised scripts have not yet been executed against the imported data.

## Project workflow

1. **Extract:** Retrieve a snapshot of Remote OK's JSON API with Python `requests`.
2. **Clean:** Remove missing title/company records, duplicate URLs and an obvious test listing; standardize dates and tags with `pandas`.
3. **Analyze:** Summarize employers, locations, listing tags, tag counts, and posting dates.
4. **Visualize:** Generate charts with `matplotlib` and examine the original Power BI report.

## Repository structure

| Path | Contents |
| --- | --- |
| [`src/extract_remoteok.py`](src/extract_remoteok.py) | API-based data collection |
| [`src/clean_jobs.py`](src/clean_jobs.py) | Cleaning and quality checks |
| [`src/visualize_jobs.py`](src/visualize_jobs.py) | Charts and skill-tag frequency export |
| `data/` | Original raw and cleaned CSV snapshots, plus skill-tag frequency table |
| `powerbi/` | Original `.pbix` dashboard and PDF preview — **to be added** |
| `docs/` | Original academic report and presentation — **to be added** |
| `images/charts/` | Generated plots after running the visualization script |

## Reproduce the Python workflow

From the repository root:

```bash
pip install -r requirements.txt
python src/extract_remoteok.py
python src/clean_jobs.py
python src/visualize_jobs.py
```

The extraction step accesses a **live API** and will produce a different snapshot over time. To reproduce the original academic analysis, use its archived dataset once uploaded instead of extracting fresh listings.

## Interpretation and limitations

- The dataset is a **snapshot of one job board**, not a representative sample of the entire global remote-job market.
- API tags may include broad descriptors such as “senior” or “support”; they should not all be interpreted as technical skills.
- The original source's salary field is not reliably standardized, so the revised cleaning script does not calculate a salary midpoint.
- Some original listing text shows encoding artifacts. Those values require source verification rather than speculative corrections.
- This repository documents an **educational analytics workflow**, not a live labor-market monitoring service.

## Original coursework

The source project, including its original code, CSVs, Power BI dashboard and academic documents, remains available at [nouhaBks/Website-Scarper](https://github.com/nouhaBks/Website-Scarper). Portfolio scripts are a refactoring of that work, not a claim that new data collection or analysis has already been completed.
