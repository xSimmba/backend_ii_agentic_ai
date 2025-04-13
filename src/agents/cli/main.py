import click
from src.agents.analysis_agent import AnalysisAgent

@click.group()
def cli():
    pass

@cli.command()
@click.argument("data")
def analyze(data):
    agent = AnalysisAgent()
    result = agent.analyze(data)
    click.echo(f"Result: {result}")

if __name__ == "__main__":
    cli()