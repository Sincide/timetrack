# Timetrack

Timetrack is a lightweight time tracking API built with **FastAPI** and **SQLModel**. It allows logging working hours, calculating flex time and overtime, and exporting weekly reports. The project is designed to run easily on a small server, such as a Hetzner VPS.

## Features
- Log daily working hours with optional overtime flag
- Compute weekly summaries showing total, flex, and overtime hours
- Export a week's data to CSV
- Simple SQLite database for quick setup

## Setup
Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Run the application in development mode:

```bash
uvicorn timetrack.main:app --reload
```

The API will be available at `http://localhost:8000`.

## Running Tests
Execute the unit tests using `pytest`:

```bash
pytest -q
```

## Endpoints
- `POST /time-log` – Parameters: `entry_date` (YYYY-MM-DD), `hours`, `overtime` (bool). Creates or updates a time entry.
- `GET /weekly-dashboard?day=YYYY-MM-DD` – Returns summary for the week containing the given day.
- `GET /export-weekly?day=YYYY-MM-DD` – Exports CSV with all entries for the week containing the given day.

## Development Log & Future Plans
See [DEVLOG.md](DEVLOG.md) for a history of development progress and [FUTURE_PLAN.md](FUTURE_PLAN.md) for planned enhancements.
