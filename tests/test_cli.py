from typer.testing import CliRunner
from calorie_analyzer.main import app
import os

runner = CliRunner()

def test_analyze_command(sample_data_path):
    result = runner.invoke(app, ["analyze", sample_data_path])
    assert result.exit_code == 0
    assert "Analysis complete." in result.stdout

def test_stats_command(sample_data_path):
    result = runner.invoke(app, ["stats", sample_data_path])
    assert result.exit_code == 0
    assert "--- General Statistics ---" in result.stdout
    assert "--- Calorie Statistics ---" in result.stdout
    assert "--- Weight Statistics ---" in result.stdout

def test_graph_command(sample_data_path):
    output_dir = "test_graphs"
    result = runner.invoke(app, ["graph", sample_data_path, "--output", output_dir])
    assert result.exit_code == 0
    assert f"Successfully generated graphs in '{output_dir}'" in result.stdout
    assert os.path.exists(output_dir)
    assert os.path.exists(os.path.join(output_dir, "weight_trend.png"))
    # Clean up created files
    for file in os.listdir(output_dir):
        os.remove(os.path.join(output_dir, file))
    os.rmdir(output_dir)

def test_tdee_command(sample_data_path):
    result = runner.invoke(app, ["tdee", sample_data_path])
    assert result.exit_code == 0
    assert "--- Maintenance Calorie (TDEE) Estimation ---" in result.stdout
    assert "Estimated Maintenance" in result.stdout
