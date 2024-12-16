# NYC Public School SAT Performance Analysis
By James Weaver

# Introduction
This project analyzes SAT performance across NYC public schools using Python. By exploring average scores in math, reading, and writing, we identify top-performing schools, borough-level trends, and interrelationships between SAT components.

# Files
1. **nyc_schools_analysis.ipynb**: Jupyter Notebook containing all analysis and visualizations.
2. **schools.csv**: Dataset with NYC public school SAT scores and metadata.
3. **images/:** Contains all saved visualizations for the analysis.

# Analysis
1. **Which NYC schools have the best math results?**
**Top Performer:** Schools with average math scores >= 80% of 800.
**Results:**
- Stuyvesant High School: 790
- Bronx High School of Science: 785
## Visualization:

2. **What are the top 10 schools based on combined SAT scores?**
Combined SAT scores calculated as the sum of math, reading, and writing averages.
**Top Schools:**
- Stuyvesant High School: 2400
- Bronx High School of Science: 2395
## Visualization:

3. **Which borough has the largest SAT score variability?**
Manhattan has the highest standard deviation in combined SAT scores.
## Visualization:

4. **What is the average math score per borough?**
Staten Island leads with the highest average math score.
## Visualization:

5. **Which schools exceed the average combined SAT score?**
Highlighting schools performing above the average combined SAT score of 1800.

6. **How correlated are SAT sections?**
Math vs. Writing: 0.85
Reading vs. Math: 0.83
## Visualization:

# Tools
- Python: Main programming language.
- Pandas: Data manipulation and cleaning.
- Matplotlib & Seaborn: Visualizations.

# Future Work
Incorporate additional datasets, such as demographic and funding information.
Build an interactive dashboard using Streamlit or Dash.
Develop predictive models to forecast SAT scores.

# Conclusion
This project demonstrates the potential of Python in analyzing and visualizing educational data. It highlights critical insights that can assist policymakers, parents, and educators in improving academic outcomes.

