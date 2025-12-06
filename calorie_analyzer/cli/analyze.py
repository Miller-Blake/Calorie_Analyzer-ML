import typer
from calorie_analyzer.core import loader, cleaner

def analyze(file: str = typer.Argument(..., help="Path to the Excel file to analyze.")):
    """
    Analyzes the given Excel file by loading and cleaning the data.
    """
    print(f"Loading data from {file}...")
    try:
        data = loader.load_data(file)
        print("Data loaded successfully.")
        
        print("Cleaning and validating data...")
        cleaned_data = cleaner.clean_data(data)
        print("Data cleaned and validated successfully.")
        
        print("\nAnalysis complete. Data is ready for further processing.")
        print("\nCleaned data preview:")
        print(cleaned_data.head())
        
    except FileNotFoundError:
        print(f"Error: File not found at {file}")
        raise typer.Exit(code=1)
    except Exception as e:
        print(f"An error occurred: {e}")
        raise typer.Exit(code=1)
