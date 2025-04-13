from fastapi import APIRouter
from src.agents.analysis_agent import AnalysisAgent

router = APIRouter()
agent = AnalysisAgent()

@router.post("/analyze")
async def analyze_data(data: dict):
    return agent.analyze(data)