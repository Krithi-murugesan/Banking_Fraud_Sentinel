from crew import run_crew
from db.setup_db import setup_banking_db

if __name__ == "__main__":
    setup_banking_db()

    print("\n--- RUNNING SENTINEL WORKFLOW ---\n")
    result = run_crew()

    print("\n\nFINAL REPORT:\n", result)
