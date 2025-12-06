# models/weights.py
from dataclasses import dataclass

@dataclass
class RegressionResult:
    """
    Represents the result of a regression analysis.
    """
    maintenance_calories: float
    confidence_range: tuple[float, float]
    r_squared: float
