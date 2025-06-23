# Timetrack

A simple time tracking API built with FastAPI. It allows logging daily hours, calculating flex and overtime, showing a weekly dashboard, and exporting weekly data.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn timetrack.main:app --reload
```

The API will be available at `http://localhost:8000`.

## Endpoints

- `POST /time-log` – parameters: `entry_date` (YYYY-MM-DD), `hours`, `overtime` (bool). Creates or updates a time entry.
- `GET /weekly-dashboard?day=YYYY-MM-DD` – returns summary for the week containing the given day.
- `GET /export-weekly?day=YYYY-MM-DD` – exports CSV with all entries for the week containing the given day.
