
from crewai import Crew, Process
from agents import get_agents
from tasks import get_tasks

def run_crew():
    forensic_architect, compliance_auditor, fraud_lead = get_agents()
    task_query, task_audit, task_report = get_tasks(
        forensic_architect, compliance_auditor, fraud_lead
    )

    crew = Crew(
        agents=[forensic_architect, compliance_auditor, fraud_lead],
        tasks=[task_query, task_audit, task_report],
        process=Process.sequential
    )

    return crew.kickoff()
