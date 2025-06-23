from datetime import date
from fastapi import FastAPI, HTTPException
from sqlmodel import select
from fastapi.responses import StreamingResponse
import csv
from io import StringIO

from .database import init_db, get_session
from .models import TimeEntry
from .utils import calculate_week_range, weekly_summary

app = FastAPI(title="Timetrack")


@app.on_event("startup")
def on_startup():
    init_db()


@app.post("/time-log")
def log_time(entry_date: date, hours: float, overtime: bool = False):
    with get_session() as session:
        entry = session.exec(select(TimeEntry).where(TimeEntry.entry_date == entry_date)).first()
        if entry:
            entry.hours = hours
            entry.overtime = overtime
        else:
            entry = TimeEntry(entry_date=entry_date, hours=hours, overtime=overtime)
            session.add(entry)
        session.commit()
        session.refresh(entry)
        return entry


@app.get("/weekly-dashboard")
def weekly_dashboard(day: date):
    start, end = calculate_week_range(day)
    with get_session() as session:
        entries = session.exec(select(TimeEntry).where(TimeEntry.entry_date.between(start, end))).all()
        summary = weekly_summary(entries)
        summary["start"] = start
        summary["end"] = end
        return summary


@app.get("/export-weekly")
def export_weekly(day: date):
    start, end = calculate_week_range(day)
    with get_session() as session:
        entries = session.exec(select(TimeEntry).where(TimeEntry.entry_date.between(start, end))).all()
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["date", "hours", "overtime"])
    for e in entries:
        writer.writerow([e.entry_date.isoformat(), e.hours, e.overtime])
    output.seek(0)
    return StreamingResponse(output, media_type="text/csv", headers={"Content-Disposition": f"attachment; filename=week_{start}.csv"})
