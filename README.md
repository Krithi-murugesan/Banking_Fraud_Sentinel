# 🏦 Banking Fraud Detection Crew (CrewAI)

This project demonstrates a **multi-agent AI workflow** using CrewAI to simulate a banking fraud detection pipeline.

It combines:

* SQL-based data analysis
* Compliance auditing (KYC checks)
* Fraud risk reporting

---

## 🚀 Overview

The system uses three specialized AI agents:

1. **Forensic SQL Architect**

   * Queries the database
   * Identifies high-value transactions in high-risk regions

2. **Compliance Auditor**

   * Reviews KYC document expiry
   * Flags regulatory violations

3. **Fraud Strategy Lead**

   * Synthesizes findings
   * Produces a final fraud risk report

---

## 🧠 Workflow

1. Query suspicious transactions
2. Audit account compliance
3. Generate a final fraud report

All tasks are executed sequentially using CrewAI orchestration.

---

## 📁 Project Structure

```
banking-fraud-crew/
│── main.py                # Entry point
│── agents.py              # Agent definitions
│── tasks.py               # Task definitions
│── crew.py                # Crew orchestration
│
├── tools/
│   └── sql_tool.py        # Custom SQLite query tool
│
├── db/
│   └── setup_db.py        # Database setup and seed data
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/banking-fraud-crew.git
cd banking-fraud-crew
```

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the full fraud detection workflow:

```bash
python main.py
```

This will:

* Create a local SQLite database (`banking_ops.db`)
* Execute all agents sequentially
* Output a final fraud risk report

---

## 🗄️ Database

The project uses a local SQLite database with two tables:

* **Accounts**

  * Account ID
  * Owner
  * KYC status
  * Document expiry date

* **Transactions**

  * Transaction ID
  * Account ID
  * Amount
  * Region
  * Timestamp

The database is automatically created and seeded at runtime.

---

## 🛠️ Tech Stack

* Python
* CrewAI
* SQLite
* SQLAlchemy
* Pandas

---

## 📊 Example Output

The system generates a report including:

* High-value transactions in high-risk regions
* Accounts with expired KYC
* Final fraud risk assessment and recommendations

---

## 🔒 Notes

* The database file (`.db`) is excluded via `.gitignore`
* This is a **simulation project** for learning/demo purposes
* No real financial data is used

---

## 🌱 Future Improvements

* Add real-time data ingestion
* Integrate with APIs
* Build a Streamlit dashboard
* Add anomaly detection models
* Deploy as a web service

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a pull request.

---

## ⭐ Acknowledgements

Built using CrewAI for multi-agent orchestration.
