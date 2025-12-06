import typer
import pandas as pd
from calorie_analyzer.core import loader, cleaner, stats_engine

def stats(file: str = typer.Argument(..., help="Path to the Excel file to calculate stats for.")):
    """
    Calculates statistics for the given Excel file.
    """
    try:
        # Load and clean data
        raw_data = loader.load_data(file)
        cleaned_data = cleaner.clean_data(raw_data)

        # Generate statistics
        stats_dict = stats_engine.generate_statistics(cleaned_data)

        # Print statistics
        typer.secho("--- General Statistics ---", fg=typer.colors.BLUE)
        typer.echo(f"Date Range: {stats_dict['start_date']} to {stats_dict['end_date']}")
        typer.echo(f"Total Days: {stats_dict['total_days']}\n")

        typer.secho("--- Calorie Statistics ---", fg=typer.colors.BLUE)
        typer.echo(f"Average Calories: {stats_dict['avg_calories']:.2f} kcal")
        typer.echo(f"Min Calories: {stats_dict['min_calories']} kcal")
        typer.echo(f"Max Calories: {stats_dict['max_calories']} kcal\n")

        typer.secho("--- Weight Statistics ---", fg=typer.colors.BLUE)
        typer.echo(f"Morning Weight (Start): {stats_dict['start_weight_morning']:.2f} lbs")
        typer.echo(f"Morning Weight (End): {stats_dict['end_weight_morning']:.2f} lbs")
        typer.echo(f"Average Morning Weight: {stats_dict['avg_weight_morning']:.2f} lbs\n")

        typer.echo(f"Night Weight (Start): {stats_dict['start_weight_night']:.2f} lbs")
        typer.echo(f"Night Weight (End): {stats_dict['end_weight_night']:.2f} lbs")
        typer.echo(f"Average Night Weight: {stats_dict['avg_weight_night']:.2f} lbs\n")

        typer.secho("--- Daily Weight Swing ---", fg=typer.colors.BLUE)
        typer.echo(f"Average Daily Swing: {stats_dict['avg_daily_swing']:.2f} lbs")
        typer.echo(f"Max Daily Swing: {stats_dict['max_daily_swing']:.2f} lbs\n")

        typer.secho("--- Correlation ---", fg=typer.colors.BLUE)
        typer.echo(f"Calorie vs. Weight Change Correlation: {stats_dict['calorie_weight_corr']:.2f}\n")

        typer.secho("--- Chipotle Statistics ---", fg=typer.colors.BLUE)
        typer.echo(f"Chipotle Days: {stats_dict['chipotle_days']} / {stats_dict['total_days']} ({stats_dict['chipotle_percentage']:.1f}%)")
        typer.echo(f"Avg Calories (Chipotle Days): {stats_dict['avg_calories_chipotle']:.2f} kcal")
        typer.echo(f"Avg Calories (No Chipotle): {stats_dict['avg_calories_no_chipotle']:.2f} kcal")
        typer.echo(f"Avg Next Day Weight Change After Chipotle: {stats_dict['avg_next_day_weight_change_after_chipotle']:.2f} lbs")

    except FileNotFoundError:
        typer.secho(f"Error: File not found at {file}", fg=typer.colors.RED)
        raise typer.Exit(code=1)
    except Exception as e:
        typer.secho(f"An error occurred: {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1)
