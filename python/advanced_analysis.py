# advanced_analysis.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Load your existing CSV (from runs_v_wins.py)
df = pd.read_csv("/Users/charliecaplinger/data-analytics/baseball/baseball_analytics/data/win-loss-record.csv")

# Create cumulative run differential per game
df['run_diff'] = df['R'] - df['RA']

# Group by year to calculate total wins and run differential
summary = df.groupby('Year').agg({
    'run_diff': 'sum',
    'W/L': lambda x: (x == 'W').sum()
}).rename(columns={'W/L': 'wins'})

# Correlation
correlation = summary['run_diff'].corr(summary['wins'])
print(f"Correlation between Run Differential and Wins: {correlation}")

# Simple regression (line of best fit)
x = summary['run_diff']
y = summary['wins']

m, b = np.polyfit(x, y, 1)

plt.scatter(x, y)
plt.plot(x, m*x + b)
plt.xlabel("Run Differential")
plt.ylabel("Wins")
plt.title("Run Differential vs Wins")
plt.show()