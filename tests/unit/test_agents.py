from src.agents.analysis_agent import AnalysisAgent

def test_analysis_agent():
    agent = AnalysisAgent()
    result = agent.analyze({"key": "value"})
    assert "insights" in result