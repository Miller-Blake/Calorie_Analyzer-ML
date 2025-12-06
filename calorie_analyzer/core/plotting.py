import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LinearRegression
import numpy as np

def generate_graphs(df: pd.DataFrame, output_dir: str):
    """
    Generates and saves a suite of graphs from the data.

    Args:
        df: Cleaned pandas DataFrame.
        output_dir: Directory to save the graph PNG files.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 1. Morning vs. Night Weight Trend
    plt.figure(figsize=(12, 6))
    plt.plot(df['date'], df['weight_morning'], label='Morning Weight', alpha=0.7)
    plt.plot(df['date'], df['weight_night'], label='Night Weight', alpha=0.7)
    plt.title('Morning vs. Night Weight')
    plt.xlabel('Date')
    plt.ylabel('Weight (lbs)')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, 'weight_trend.png'))
    plt.close()

    # 2. 7-Day Moving Average of Average Weight
    df['avg_weight_7day'] = df['avg_weight'].rolling(window=7).mean()
    plt.figure(figsize=(12, 6))
    plt.plot(df['date'], df['avg_weight'], label='Daily Average Weight', alpha=0.5)
    plt.plot(df['date'], df['avg_weight_7day'], label='7-Day Moving Average', color='red', linewidth=2)
    plt.title('7-Day Moving Average of Weight')
    plt.xlabel('Date')
    plt.ylabel('Weight (lbs)')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, 'weight_moving_average.png'))
    plt.close()

    # 3. Calorie Intake Trend
    plt.figure(figsize=(12, 6))
    plt.plot(df['date'], df['calories'], label='Daily Calorie Intake', color='green')
    plt.title('Calorie Intake Trend')
    plt.xlabel('Date')
    plt.ylabel('Calories (kcal)')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, 'calorie_trend.png'))
    plt.close()

    # 4. Calorie vs. Delta-Weight Scatter Plot + Regression Line
    df_reg = df.dropna(subset=['calories', 'delta_weight'])
    X = df_reg[['calories']]
    y = df_reg['delta_weight']
    
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, alpha=0.6, label='Daily Data')
    plt.plot(X, y_pred, color='red', linewidth=2, label='Regression Line')
    plt.title('Calories vs. Daily Weight Change')
    plt.xlabel('Calories (kcal)')
    plt.ylabel('Change in Avg Weight (lbs)')
    plt.axhline(0, color='black', linestyle='--', linewidth=1)
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, 'calorie_vs_delta_weight.png'))
    plt.close()

    # 5. Daily Weight Swing Bar Chart
    df['daily_swing'] = df['weight_night'] - df['weight_morning']
    plt.figure(figsize=(12, 6))
    plt.bar(df['date'], df['daily_swing'], color='purple', alpha=0.7)
    plt.title('Daily Weight Swing (Night - Morning)')
    plt.xlabel('Date')
    plt.ylabel('Weight Swing (lbs)')
    plt.grid(axis='y')
    plt.savefig(os.path.join(output_dir, 'daily_swing.png'))
    plt.close()

    print(f"Graphs saved to '{output_dir}' directory.")
