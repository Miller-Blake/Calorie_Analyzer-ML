import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from typing import Dict, Any

def estimate_tdee(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Estimates Maintenance Calories (TDEE) using two linear regression models.

    Args:
        df: A cleaned pandas DataFrame with 'calories' and 'delta_weight' columns.

    Returns:
        A dictionary containing the results from both regression models,
        including maintenance calorie estimates, confidence ranges, and R^2 scores.
    """
    results = {}
    df_reg = df.dropna(subset=['calories', 'delta_weight'])

    if len(df_reg) < 10: # Need sufficient data for regression
        return {
            "error": "Not enough data for regression analysis (requires at least 10 days with complete data)."
        }

    # --- Model A: Baseline (calories only) ---
    X_base = df_reg[['calories']]
    y = df_reg['delta_weight']
    
    model_base = LinearRegression()
    model_base.fit(X_base, y)
    
    slope_base = model_base.coef_[0]
    intercept_base = model_base.intercept_
    
    if slope_base == 0:
        maintenance_calories_base = float('inf') # Avoid division by zero
    else:
        maintenance_calories_base = -intercept_base / slope_base
        
    r_squared_base = model_base.score(X_base, y)
    
    # --- Model B: Chipotle-Adjusted (calories + chipotle) ---
    X_chipotle = df_reg[['calories', 'chipotle']]
    
    model_chipotle = LinearRegression()
    model_chipotle.fit(X_chipotle, y)
    
    calories_coef, chipotle_coef = model_chipotle.coef_
    intercept_chipotle = model_chipotle.intercept_
    
    if calories_coef == 0:
        maintenance_calories_chipotle = float('inf')
    else:
        # TDEE is where delta_weight = 0 for a non-chipotle day (chipotle=0)
        maintenance_calories_chipotle = -intercept_chipotle / calories_coef

    r_squared_chipotle = model_chipotle.score(X_chipotle, y)

    # Calculate confidence interval (simple version using residual standard error)
    y_pred = model_base.predict(X_base)
    residuals = y - y_pred
    residual_std_err = np.sqrt(np.sum(residuals**2) / (len(df_reg) - 2))
    # For a 95% CI, z-score is ~1.96
    margin_of_error_weight = 1.96 * residual_std_err
    # Convert weight error to calorie error
    margin_of_error_calories = margin_of_error_weight / abs(slope_base) if slope_base != 0 else 0

    results['baseline_maintenance'] = maintenance_calories_base
    results['baseline_r2'] = r_squared_base
    results['baseline_confidence_range'] = (
        maintenance_calories_base - margin_of_error_calories,
        maintenance_calories_base + margin_of_error_calories
    )
    results['chipotle_adjusted_maintenance'] = maintenance_calories_chipotle
    results['chipotle_adjusted_r2'] = r_squared_chipotle
    results['chipotle_effect_lbs'] = chipotle_coef
    
    return results
