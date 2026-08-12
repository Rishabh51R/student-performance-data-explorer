# Student Performance Data Explorer

## AI/ML Internship — Task 1

### Project Objective
This project performs exploratory data analysis (EDA) on student performance data using Python, Pandas, NumPy, Matplotlib, and Seaborn.

The workflow includes:
- Data loading
- Data inspection
- Missing-value analysis and cleaning
- Duplicate detection and removal
- Descriptive statistics
- Mean, median, and mode
- Histogram
- Scatter plot
- Box plots
- Correlation analysis
- Correlation heatmap
- Findings and conclusion

## Dataset
The dataset contains 122 records before cleaning and 7 columns.

Columns:
- Student_Name
- Study_Hours
- Attendance_Percent
- Assignment_Score
- Python_Score
- ML_Score
- Final_Score

## Data Cleaning
- Missing cells before cleaning: 5
- Numeric missing values were filled using the median of the respective column.
- Duplicate rows removed: 2
- Final cleaned dataset: 120 rows.

## Key Findings
- Average Final Score: 70.81
- Median Final Score: 71.55
- Highest Final Score: 89.3
- Lowest Final Score: 55.0
- Study Hours vs Final Score correlation: 0.64
- Attendance vs Final Score correlation: 0.14
- Strongest correlation with Final Score: ML_Score (0.66)

## Project Structure

```text
student_performance_data_explorer/
├── data/
│   └── student_performance.csv
├── notebooks/
│   └── Student_Performance_Data_Explorer.ipynb
├── assets/
│   ├── 01_final_score_histogram.png
│   ├── 02_study_hours_vs_final_score.png
│   ├── 03_score_boxplots.png
│   └── 04_correlation_heatmap.png
├── reports/
│   ├── actual_findings.md
│   └── execution_summary.json
├── src/
└── README.md
```

## How to Run
1. Install Python 3.12+.
2. Install the required packages:
   `pip install pandas numpy matplotlib seaborn jupyter`
3. Open the `notebooks` folder in Jupyter Notebook.
4. Run `Student_Performance_Data_Explorer.ipynb` from top to bottom.

## Conclusion
The analysis demonstrates a complete beginner-level EDA workflow. The generated charts help understand score distributions, relationships between study hours and final scores, possible outliers, and correlations among numeric variables.

> Correlation indicates association; it does not by itself prove causation.
