import pandas as pd
from typing import Dict, Any

def generate_statistics(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Generates a dictionary of statistics from the cleaned DataFrame.

    Args:
        df: A cleaned pandas DataFrame.

    Returns:
        A dictionary containing key statistics.
    """
    stats = {}

    # Date range
    stats['start_date'] = df['date'].min().strftime('%Y-%m-%d')
    stats['end_date'] = df['date'].max().strftime('%Y-%m-%d')
    stats['total_days'] = (df['date'].max() - df['date'].min()).days + 1

    # Calorie statistics
    stats['avg_calories'] = df['calories'].mean()
    stats['min_calories'] = df['calories'].min()
    stats['max_calories'] = df['calories'].max()

    # Weight statistics
    stats['start_weight_morning'] = df['weight_morning'].iloc[0]
    stats['end_weight_morning'] = df['weight_morning'].iloc[-1]
    stats['avg_weight_morning'] = df['weight_morning'].mean()
    stats['start_weight_night'] = df['weight_night'].iloc[0]
    stats['end_weight_night'] = df['weight_night'].iloc[-1]
    stats['avg_weight_night'] = df['weight_night'].mean()

    # Daily swing
    df['daily_swing'] = df['weight_night'] - df['weight_morning']
    stats['avg_daily_swing'] = df['daily_swing'].mean()
    stats['max_daily_swing'] = df['daily_swing'].max()

    # Correlation
    stats['calorie_weight_corr'] = df['calories'].corr(df['delta_weight'])

    # Chipotle statistics
    chipotle_days = df[df['chipotle'] == True]
    non_chipotle_days = df[df['chipotle'] == False]
    stats['chipotle_days'] = len(chipotle_days)
    stats['chipotle_percentage'] = (len(chipotle_days) / len(df)) * 100 if len(df) > 0 else 0
    stats['avg_calories_chipotle'] = chipotle_days['calories'].mean() if len(chipotle_days) > 0 else 0
    stats['avg_calories_no_chipotle'] = non_chipotle_days['calories'].mean() if len(non_chipotle_days) > 0 else 0
    stats['avg_next_day_weight_change_after_chipotle'] = chipotle_days['delta_weight'].mean() if len(chipotle_days) > 0 else 0

    return stats
