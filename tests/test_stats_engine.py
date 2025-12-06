import pytest
from calorie_analyzer.core import stats_engine

def test_generate_statistics(sample_dataframe):
    """Tests the statistics generation function."""
    # First, clean the data as the stats engine expects cleaned data
    from calorie_analyzer.core.cleaner import clean_data
    cleaned_df = clean_data(sample_dataframe)
    
    stats = stats_engine.generate_statistics(cleaned_df)
    
    # Check for key statistics
    assert 'start_date' in stats
    assert 'avg_calories' in stats
    assert 'chipotle_days' in stats
    
    # Check some values
    assert stats['total_days'] == 15
    # The avg_calories will change based on the generated data, so we can't assert an exact value
    # But we can check its type and if it's a reasonable number
    assert isinstance(stats['avg_calories'], (int, float))
    assert stats['avg_calories'] > 0 
