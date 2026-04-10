import os
import sqlite3

DB_FILE = "banking_ops.db"

def setup_banking_db(reset: bool = True):
    """
    Creates and seeds the banking database.

    Args:
        reset (bool): If True, deletes existing DB and recreates it.
    """

    # Delete existing DB (for clean runs)
    if reset and os.path.exists(DB_FILE):
        os.remove(DB_FILE)

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # --- Create Tables ---
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Accounts (
            acc_id INTEGER PRIMARY KEY,
            owner TEXT,
            kyc_status TEXT,
            doc_expiry DATE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Transactions (
            id INTEGER PRIMARY KEY,
            acc_id INTEGER,
            amount FLOAT,
            region TEXT,
            time TIMESTAMP,
            FOREIGN KEY (acc_id) REFERENCES Accounts(acc_id)
        )
    """)

    # --- Seed Data ---
    cursor.execute("""
        INSERT INTO Accounts (acc_id, owner, kyc_status, doc_expiry) VALUES
        (888, 'John Doe', 'Verified', '2027-01-01'),
        (999, 'Unknown Entity', 'Verified', '2024-12-01')
    """)

    cursor.execute("""
        INSERT INTO Transactions (id, acc_id, amount, region, time) VALUES
        (1, 888, 12000.0, 'High-Risk', '2026-04-06 17:15:00'),
        (2, 999, 15500.0, 'High-Risk', '2026-04-06 17:45:00')
    """)

    conn.commit()
    conn.close()

    print(f"✅ Database setup complete: {DB_FILE}")


# Optional: allow standalone execution
if __name__ == "__main__":
    setup_banking_db()
