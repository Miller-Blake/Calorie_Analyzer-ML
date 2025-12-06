import pytest
import pandas as pd
from calorie_analyzer.core import cleaner

def test_clean_data(sample_dataframe):
    """Tests the data cleaning and validation function."""
    cleaned_df = cleaner.clean_data(sample_dataframe)
    
    # Check for correct dtypes
    assert pd.api.types.is_datetime64_any_dtype(cleaned_df['date'])
    assert pd.api.types.is_numeric_dtype(cleaned_df['calories'])
    assert pd.api.types.is_bool_dtype(cleaned_df['chipotle'])
    
    # Check for feature engineering
    assert 'avg_weight' in cleaned_df.columns
    assert 'delta_weight' in cleaned_df.columns
    
    # Check that there are no missing values in key columns
    assert not cleaned_df[['calories', 'weight_morning', 'weight_night']].isnull().values.any()

def test_clean_data_missing_column():
    """Tests that a ValueError is raised if a required column is missing."""
    df = pd.DataFrame({'calories': [2000, 2500]})
    with pytest.raises(ValueError):
        cleaner.clean_data(df)
