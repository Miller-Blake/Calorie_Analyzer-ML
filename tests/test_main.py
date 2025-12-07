# tests/test_main.py

from typer.testing import CliRunner
from calorie_analyzer.main import app

runner = CliRunner()

def test_app():
    result = runner.invoke(app, ["--help"], color=False)
    assert result.exit_code == 0
    assert "Usage:" in result.stdout
    assert "[OPTIONS]" in result.stdout
    assert "COMMAND" in result.stdout
    assert "analyze" in result.stdout
    assert "stats" in result.stdout
    assert "graph" in result.stdout
    assert "tdee" in result.stdout
