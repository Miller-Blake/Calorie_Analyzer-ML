import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """
    Loads data from an Excel file into a pandas DataFrame.

    Args:
        file_path: The path to the Excel file.

    Returns:
        A pandas DataFrame containing the loaded data.
    """
    try:
        df = pd.read_excel(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        raise
    except Exception as e:
        print(f"An unexpected error occurred while reading the Excel file: {e}")
        raise
