import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from fastapi.testclient import TestClient
from timetrack.main import app


def test_log_and_dashboard():
    with TestClient(app) as client:
        response = client.post(
            "/time-log",
            params={"entry_date": "2024-01-01", "hours": 10, "overtime": False},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["hours"] == 10

        response = client.get("/weekly-dashboard", params={"day": "2024-01-01"})
        assert response.status_code == 200
        summary = response.json()
        assert summary["total_hours"] == 10
        assert summary["flex_hours"] == 2
        assert summary["overtime_hours"] == 0
