
from crewai import Task

def get_tasks(forensic_architect, compliance_auditor, fraud_lead):
    
    task_query = Task(
        description="Find high-risk transactions > 10,000 with owner names.",
        expected_output="Table of transactions.",
        agent=forensic_architect
    )

    task_audit = Task(
        description="Check for KYC expiry before 2026-04-06.",
        expected_output="List of violations.",
        agent=compliance_auditor,
        context=[task_query]
    )

    task_report = Task(
        description="Generate fraud risk report in Markdown.",
        expected_output="Final report.",
        agent=fraud_lead,
        context=[task_query, task_audit]
    )

    return task_query, task_audit, task_report
