import pytest
import pandas as pd
import os
from datetime import timedelta

@pytest.fixture(scope="session")
def sample_data_path():
    """Returns the path to the sample data excel file."""
    # Assuming sample_data.xlsx is in the is4010-final-calorie-analyzer directory
    return os.path.join(os.path.dirname(__file__), "..", "sample_data.xlsx")

@pytest.fixture(scope="session")
def sample_dataframe():
    """Returns a sample DataFrame for testing with at least 10 entries."""
    dates = []
    start_date = pd.to_datetime('2023-01-01')
    for i in range(15): # Generate 15 days of data
        dates.append(start_date + timedelta(days=i))
    
    data = {
        'date': dates,
        'calories': [2000 + i*10 for i in range(15)],
        'weight_morning': [180.0 + i*0.1 - (i//5)*0.5 for i in range(15)], # Some variation
        'weight_night': [181.0 + i*0.1 - (i//5)*0.5 for i in range(15)],   # Some variation
        'chipotle': [bool(i % 3 == 0) for i in range(15)], # Every 3rd day is chipotle
        'notes': ['' for _ in range(15)],
        'steps': [5000 + i*100 for i in range(15)],
        'protein': [150 + i*2 for i in range(15)]
    }
    return pd.DataFrame(data)
