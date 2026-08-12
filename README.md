# Student Performance Data Explorer

## AI/ML Internship — Task 1

This project performs Exploratory Data Analysis (EDA) on student performance data using Python, Pandas, NumPy and Matplotlib.

### Analysis performed
- Data loading and inspection
- Missing-value and duplicate checks
- Data cleaning
- Descriptive statistics
- Mean, median and mode
- Histogram
- Scatter plot
- Box plots
- Correlation analysis
- Correlation heatmap
- Findings and conclusion

## Dataset
The actual uploaded dataset contains **20 student records and 7 columns**.

Columns:
`student_id`, `gender`, `study_hours`, `attendance_percent`, `previous_score`, `assignments_completed`, `final_score`

## Data Cleaning
- Missing cells: **0**
- Duplicate rows: **0**
- Cleaned dataset: **20 rows**

## Actual Findings
- Average final score: **77.55**
- Median final score: **77.50**
- Mode final score: **53.00**
- Highest final score: **98.00**
- Lowest final score: **53.00**
- Average study hours: **4.42**
- Average attendance: **84.65%**
- Study hours vs final score correlation: **0.99**
- Attendance vs final score correlation: **0.98**
- Previous score vs final score correlation: **1.00**
- Assignments completed vs final score correlation: **0.97**

The strongest correlation with final score among these numeric predictors is **previous score (1.00)**.

> Correlation indicates association; it does not by itself prove causation.

## How to Run
Install:
`pip install pandas numpy matplotlib seaborn jupyter`

Open `Student_Performance_Data_Explorer.ipynb` and run all cells from top to bottom.
