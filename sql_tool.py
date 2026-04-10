from crewai.tools import BaseTool
from sqlalchemy import create_engine, text
import pandas as pd

class SQLiteQueryTool(BaseTool):
    name: str = "query_banking_db"
    description: str = "Run SQL queries against the banking database."

    def _run(self, sql_query: str) -> str:
        try:
            query = sql_query.replace("```sql", "").replace("```", "").strip()
            engine = create_engine('sqlite:///banking_ops.db')
            with engine.connect() as connection:
                df = pd.read_sql_query(text(query), connection)
                return df.to_string()
        except Exception as e:
            return f"Error executing query: {str(e)}"

sql_tool = SQLiteQueryTool()
