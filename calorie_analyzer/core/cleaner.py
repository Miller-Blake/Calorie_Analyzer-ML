import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and validates the loaded DataFrame.

    This function performs the following operations:
    - Checks for required columns.
    - Converts 'date' column to datetime objects.
    - Converts 'calories', 'weight_morning', and 'weight_night' to numeric, coercing errors.
    - Normalizes the 'chipotle' column to boolean values (True/False).
    - Fills missing weight values using forward fill.
    - Calculates 'avg_weight' and 'delta_weight'.

    Args:
        df: The raw pandas DataFrame.

    Returns:
        A cleaned and prepared pandas DataFrame.
    """
    required_columns = ['date', 'calories', 'weight_morning', 'weight_night', 'chipotle']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # Convert 'date' column
    df['date'] = pd.to_datetime(df['date'])

    # Convert numeric columns
    numeric_cols = ['calories', 'weight_morning', 'weight_night']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Normalize 'chipotle' column
    df['chipotle'] = df['chipotle'].apply(
        lambda x: str(x).strip().upper() in ['TRUE', '1', 'YES', 'T']
    )

    # Handle missing weight data
    df['weight_morning'] = df['weight_morning'].ffill()
    df['weight_night'] = df['weight_night'].ffill()
    df.dropna(subset=numeric_cols, inplace=True) # Drop any remaining NaNs

    # Feature engineering
    df['avg_weight'] = (df['weight_morning'] + df['weight_night']) / 2
    df['delta_weight'] = df['avg_weight'].diff().shift(-1) # Daily change in average weight

    return df
