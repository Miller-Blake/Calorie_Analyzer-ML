import pytest
from calorie_analyzer.core import loader
import pandas as pd

def test_load_data(sample_data_path):
    """Tests that data is loaded correctly from an Excel file."""
    df = loader.load_data(sample_data_path)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

def test_load_data_file_not_found():
    """Tests that a FileNotFoundError is raised for a non-existent file."""
    with pytest.raises(FileNotFoundError):
        loader.load_data("non_existent_file.xlsx")
