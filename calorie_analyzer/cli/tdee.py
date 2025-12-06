import typer
from calorie_analyzer.core import loader, cleaner, regression

def tdee(file: str = typer.Argument(..., help="Path to the Excel file to estimate TDEE from.")):
    """
    Estimates TDEE (Total Daily Energy Expenditure) using regression analysis.
    """
    try:
        # Load and clean data
        raw_data = loader.load_data(file)
        cleaned_data = cleaner.clean_data(raw_data)

        # Estimate TDEE
        tdee_results = regression.estimate_tdee(cleaned_data)

        if "error" in tdee_results:
            typer.secho(f"Error: {tdee_results['error']}", fg=typer.colors.RED)
            raise typer.Exit(code=1)

        # Print results
        typer.secho("--- Maintenance Calorie (TDEE) Estimation ---", fg=typer.colors.GREEN)
        
        typer.echo("\n--- Baseline Model (Calories Only) ---")
        typer.echo(f"Estimated Maintenance: {tdee_results['baseline_maintenance']:.0f} kcal/day")
        typer.echo(f"95% Confidence Range: {tdee_results['baseline_confidence_range'][0]:.0f} - {tdee_results['baseline_confidence_range'][1]:.0f} kcal/day")
        typer.echo(f"Model R-squared: {tdee_results['baseline_r2']:.2f}")

        typer.echo("\n--- Chipotle-Adjusted Model ---")
        typer.echo(f"Adjusted Maintenance: {tdee_results['chipotle_adjusted_maintenance']:.0f} kcal/day")
        typer.echo(f"Chipotle Effect on Next-Day Weight: {tdee_results['chipotle_effect_lbs']:+.2f} lbs")
        typer.echo(f"Model R-squared: {tdee_results['chipotle_adjusted_r2']:.2f}")

        typer.echo("\nThis model estimates the calorie level at which your weight would theoretically remain stable based on the provided data.")

    except FileNotFoundError:
        typer.secho(f"Error: File not found at {file}", fg=typer.colors.RED)
        raise typer.Exit(code=1)
    except Exception as e:
        typer.secho(f"An error occurred: {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1)
