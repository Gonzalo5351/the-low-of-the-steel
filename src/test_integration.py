# src/test_integration.py
from datetime import date, timedelta
from storage import save_log
from analyzer import load_data
from analyzer import analyze

def simulate_week():
    base_date = date.today()
    for i in range(7):
        fake_day = str(base_date - timedelta(days=i))
        entry = {
            "wake_up": i % 2 == 0,
            "exercised": i % 3 != 0,
            "ate_clean": i != 6,
            "note": f"Simulated day {i + 1}"
        }
        save_log(fake_day, entry)

    print("\n=== Simulated Summary ===")
    analyze(load_data())

if __name__ == "__main__":
    simulate_week()
