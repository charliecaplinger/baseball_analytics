# ⚾ Baseball Analytics (Python Data Analysis Project)

## Overview

This project analyzes MLB team performance using Python by combining game-level results, run differential, and advanced metrics like WAR (Wins Above Replacement).

The analysis focuses on identifying how team performance evolves throughout a season and how advanced metrics like WAR correlate with team success.

Data is sourced using the `pybaseball` library and processed using Python for analysis and visualization.

---

## Tools & Technologies

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- pybaseball  

---

## Key Objectives

- Analyze team performance trends over multiple seasons  
- Evaluate the relationship between **run differential and wins**  
- Compare team performance using **WAR across the league**  
- Identify how elite teams compare to league averages  

---

## Data Collection

Data was collected using the `pybaseball` library:

- Game-level data (wins/losses, runs scored, runs allowed) :contentReference[oaicite:0]{index=0}  
- Player-level batting and pitching statistics :contentReference[oaicite:1]{index=1}  

Seasons analyzed include:

- 2019, 2021, 2022, 2023, 2024, 2025 (St. Louis Cardinals trends)  
- League-wide WAR analysis for 2022 and 2025  

---

## Data Preparation

- Removed unnecessary columns (e.g., Attendance)  
- Combined multiple seasons into a unified dataset  
- Created cumulative metrics:
  - Win count over time  
  - Run differential (Runs Scored – Runs Allowed)  
- Aggregated player WAR to calculate **team-level WAR**  

---

## Key Analysis

### 1. Win Trends Over Time

- Calculated cumulative wins across multiple Cardinals seasons  
- Visualized how different teams progressed throughout each season  

📊 Insight:
- Stronger seasons show **consistent upward win trends**, while weaker seasons plateau earlier  
- Comparing multiple years highlights **season-to-season variability in team performance**

---

### 2. Run Differential Analysis

- Calculated cumulative run differential throughout each season  
- Compared how scoring vs defense impacts overall performance  

📊 Insight:
- Teams with consistently positive run differential tend to have stronger win trajectories  
- Run differential acts as a strong indicator of **true team performance beyond record**

---

### 3. Team WAR Analysis (League-Wide)

- Aggregated **batting WAR + pitching WAR** for each team  
- Calculated total team WAR for 2022 and 2025  
- Compared selected teams against league average  

📊 Insight:
- Teams like the **Dodgers, Yankees, and Phillies** consistently rank above average in total WAR  
- High-performing teams show strong contributions from both **offense and pitching**  
- Teams near or below average WAR tend to have less consistent performance  

---

### 4. League Benchmarking

- Calculated average team WAR across all 30 MLB teams  
- Compared individual teams to league baseline  

📊 Insight:
- League average provides a clear benchmark for identifying **contenders vs average teams**  
- Top teams significantly outperform the average, reinforcing WAR as a strong performance indicator  

---

## Data Visualization

The project includes multiple visualizations:

- 📈 Cumulative win trends across seasons  
- 📉 Run differential over time  
- 📊 Team WAR comparisons vs league average  

These visualizations highlight how performance evolves and how teams compare across key metrics.

---

## Key Insights

- **Run differential strongly correlates with winning performance** over a season  
- **Consistent performance over time** is a defining trait of successful teams  
- **WAR is an effective metric** for evaluating overall team strength  
- Elite teams (e.g., Dodgers, Yankees) consistently outperform league averages  
- Team success is driven by a **balance of offensive and pitching contributions**

---

## Skills Demonstrated

- Data Collection (API-based using pybaseball)  
- Data Cleaning & Transformation  
- Exploratory Data Analysis (EDA)  
- Feature Engineering (cumulative metrics, WAR aggregation)  
- Data Visualization  
- Sports Analytics / Performance Analysis  

---

## Project Structure



---

## Future Improvements

- Add correlation analysis between WAR and wins  
- Build predictive models for team performance  
- Integrate more advanced metrics (OPS, wOBA, xERA)  
- Create an interactive dashboard (Tableau or web app)  

---

## Conclusion

This project demonstrates how Python can be used to analyze real-world sports data and uncover meaningful insights about team performance.

By combining traditional statistics (wins, runs) with advanced metrics (WAR), this analysis provides a deeper understanding of what drives success in baseball.
