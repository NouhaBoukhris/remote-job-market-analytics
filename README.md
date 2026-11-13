# Remote Job Market Analytics | Python & Power BI

**API data extraction · Data cleaning · Exploratory analysis · Power BI**

An academic project exploring remote-job listings, reported locations, employers, and recurring skill tags. Data was obtained from the [Remote OK API](https://remoteok.com/api).

## Project workflow

1. **Extract:** Retrieve a snapshot of Remote OK's JSON API with Python `requests`.
2. **Clean:** Remove missing title/company records, duplicate URLs and an obvious test listing; standardize dates and tags with `pandas`.
3. **Analyze:** Summarize employers, locations, listing tags, tag counts, and posting dates.
4. **Visualize:** Generate charts with `matplotlib` and examine the original Power BI report.

## Power BI dashboard

The original interactive Power BI report is available as [`scraper.pbix`](powerbi/scraper.pbix). For a quick view without Power BI Desktop, open the [dashboard PDF preview](powerbi/Scraper%20Power%20BI%20Dashboard.pdf).

> A dashboard screenshot will be embedded here after a PNG image is added to `images/`.

## Repository structure

| Path | Contents |
| --- | --- |
| [`src/extract_remoteok.py`](src/extract_remoteok.py) | API-based data collection |
| [`src/clean_jobs.py`](src/clean_jobs.py) | Cleaning and quality checks |
| [`src/visualize_jobs.py`](src/visualize_jobs.py) | Charts and skill-tag frequency export |
| `data/` | Original raw and cleaned CSV snapshots, plus skill-tag frequency table |
| `powerbi/` | Original `.pbix` dashboard and PDF preview — **to be added** |
| `docs/` | Final academic report and presentation |
| `images/charts/` | Generated plots after running the visualization script |

## Reproduce the Python workflow

From the repository root:

```bash
pip install -r requirements.txt
python src/extract_remoteok.py
python src/clean_jobs.py
python src/visualize_jobs.py
```

The extraction step accesses a **live API** and will produce a different snapshot over time. To reproduce the academic analysis, use the included archived dataset instead of extracting fresh listings.

## Interpretation and limitations

- The dataset is a **snapshot of one job board**, not a representative sample of the entire global remote-job market.
- API tags may include broad descriptors such as “senior” or “support”; they should not all be interpreted as technical skills.
- The original source's salary field is not reliably standardized, so the revised cleaning script does not calculate a salary midpoint.
- Some original listing text shows encoding artifacts. Those values require source verification rather than speculative corrections.
- This repository documents an **educational analytics workflow**, not a live labor-market monitoring service.

## Documentation

- [Final project report](docs/Final_Report.pdf)
- [Final presentation](docs/Final_Presentation.pdf)

## Project context

This project was developed as academic coursework. The Python workflow has been reorganized for readability and reproducibility; the updated scripts have not yet been execution-tested.
