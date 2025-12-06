import typer
from calorie_analyzer.cli import analyze, stats, graph, tdee

app = typer.Typer(help="Calorie and weight analysis CLI tool.")

app.command()(analyze.analyze)
app.command()(stats.stats)
app.command()(graph.graph)
app.command()(tdee.tdee)

if __name__ == "__main__":
    app()