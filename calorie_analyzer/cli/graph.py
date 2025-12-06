import typer
from calorie_analyzer.core import loader, cleaner, plotting
import os

def graph(
    file: str = typer.Argument(..., help="Path to the Excel file to generate graphs from."),
    output: str = typer.Option("graphs", "--output", help="Path to save the graph files.")
):
    """
    Generates graphs for the given Excel file.
    """
    try:
        # Load and clean data
        raw_data = loader.load_data(file)
        cleaned_data = cleaner.clean_data(raw_data)

        # Define output directory
        output_dir = output or "graphs"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Generate and save graphs
        plotting.generate_graphs(cleaned_data, output_dir)
        typer.secho(f"Successfully generated graphs in '{output_dir}'.", fg=typer.colors.GREEN)

    except FileNotFoundError:
        typer.secho(f"Error: File not found at {file}", fg=typer.colors.RED)
        raise typer.Exit(code=1)
    except Exception as e:
        typer.secho(f"An error occurred: {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1)
