from celery import Celery

app = Celery("agentic_tasks", broker="redis://localhost:6379/0")

@app.task
def async_analyze(data):
    from src.agents.analysis_agent import AnalysisAgent
    return AnalysisAgent().analyze(data)