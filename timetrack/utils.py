from datetime import date, timedelta
from typing import List
from .models import TimeEntry


def calculate_week_range(d: date) -> (date, date):
    """Return Monday-Sunday range for week containing date d."""
    start = d - timedelta(days=d.weekday())
    end = start + timedelta(days=6)
    return start, end


def weekly_summary(entries: List[TimeEntry]):
    total_hours = sum(e.hours for e in entries)
    overtime_hours = sum(max(0, e.hours - 8) if e.overtime else 0 for e in entries)
    flex_hours = sum(max(0, e.hours - 8) if not e.overtime else 0 for e in entries)
    return {
        "days": len(entries),
        "total_hours": total_hours,
        "overtime_hours": overtime_hours,
        "flex_hours": flex_hours,
    }
