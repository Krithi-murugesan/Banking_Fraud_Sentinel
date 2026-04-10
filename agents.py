
from crewai import Agent
from tools.sql_tool import sql_tool

def get_agents():
    forensic_architect = Agent(
        role='Forensic SQL Architect',
        goal='Identify high-value transactions using the database tool.',
        backstory='Expert in SQLite financial analysis.',
        tools=[sql_tool],
        verbose=True
    )

    compliance_auditor = Agent(
        role='Compliance Auditor',
        goal='Flag expired KYC documents.',
        backstory='Expert in regulatory compliance.',
        verbose=True
    )

    fraud_lead = Agent(
        role='Fraud Strategy Lead',
        goal='Summarize fraud risks and recommend actions.',
        backstory='Decision-maker for fraud prevention.',
        verbose=True
    )

    return forensic_architect, compliance_auditor, fraud_lead
