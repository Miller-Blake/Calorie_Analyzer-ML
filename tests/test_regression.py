import pytest
from calorie_analyzer.core import regression
import numpy as np

def test_estimate_tdee(sample_dataframe):
    """Tests the TDEE estimation function with sufficient data."""
    from calorie_analyzer.core.cleaner import clean_data
    cleaned_df = clean_data(sample_dataframe)
    
    results = regression.estimate_tdee(cleaned_df)
    
    assert 'baseline_maintenance' in results
    assert 'chipotle_adjusted_maintenance' in results
    assert 'baseline_r2' in results
    assert 'chipotle_effect_lbs' in results

    # Check that the values are numbers and not NaN/inf
    assert isinstance(results['baseline_maintenance'], (int, float, np.number))
    assert not np.isnan(results['baseline_maintenance'])
    assert not np.isinf(results['baseline_maintenance'])

    assert isinstance(results['chipotle_adjusted_maintenance'], (int, float, np.number))
    assert not np.isnan(results['chipotle_adjusted_maintenance'])
    assert not np.isinf(results['chipotle_adjusted_maintenance'])
