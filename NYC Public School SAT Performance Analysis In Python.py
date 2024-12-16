#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# Set visualization styles
sns.set(style="whitegrid")


# In[3]:


# Read in the data
schools = pd.read_csv("schools.csv")


# In[4]:


# Preview the dataset
print("Dataset Preview:")
schools.head()


# ## SECTION 1: NYC Schools with Best Math Results

# In[6]:


print("\nBest Performing Schools in Math (>= 80% of 800):")
best_math_schools = schools[schools['average_math'] >= 0.8 * 800]
best_math_schools = best_math_schools.sort_values('average_math', ascending=False)
best_math_results = best_math_schools[['school_name', 'average_math']]
best_math_results.head(10)


# ## Visualization: Top 10 Math Scores

# In[8]:


plt.figure(figsize=(10, 6))
sns.barplot(data=best_math_results.head(10), x='average_math', y='school_name', palette="coolwarm")
plt.title("Top 10 Schools with Best Math Scores")
plt.xlabel("Average Math Score")
plt.ylabel("School Name")
plt.tight_layout()
plt.savefig("top_math_scores.png")
plt.show()


# ## SECTION 2: Top 10 Schools Based on Combined SAT Scores

# In[10]:


schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']
top_10_schools = schools.sort_values('total_SAT', ascending=False).head(10)
print("\nTop 10 Schools by Combined SAT Scores:")
top_10_schools[['school_name', 'total_SAT']]


# ## Visualization: Top 10 Combined SAT Scores

# In[11]:


plt.figure(figsize=(10, 6))
sns.barplot(data=top_10_schools, x='total_SAT', y='school_name', palette="viridis")
plt.title("Top 10 Schools by Combined SAT Scores")
plt.xlabel("Total SAT Score")
plt.ylabel("School Name")
plt.tight_layout()
plt.savefig("top_combined_scores.png")
plt.show()


# ## SECTION 3: Borough with the Largest SAT Score Standard Deviation

# In[13]:


borough_stats = schools.groupby('borough')['total_SAT'].agg(['count', 'mean', 'std']).round(2)
largest_std_borough = borough_stats.loc[borough_stats['std'].idxmax()]
print("\nBorough with Largest Standard Deviation in SAT Scores:")
largest_std_borough


# ## Visualization: Borough SAT Statistics

# In[14]:


plt.figure(figsize=(8, 5))
borough_stats.sort_values('std', ascending=False)['std'].plot(kind='bar', color='steelblue')
plt.title("Standard Deviation of SAT Scores by Borough")
plt.xlabel("Borough")
plt.ylabel("Standard Deviation")
plt.tight_layout()
plt.savefig("borough_sat_std.png")
plt.show()


# ## Average Math Score per Borough

# In[17]:


avg_math_borough = schools.groupby('borough')['average_math'].mean().round(2)
print("\nAverage Math Scores by Borough:")
avg_math_borough


# ## Visualization: Average Math Scores by Borough

# In[18]:


plt.figure(figsize=(8, 5))
avg_math_borough.sort_values(ascending=False).plot(kind='bar', color='darkorange')
plt.title("Average Math Scores by Borough")
plt.xlabel("Borough")
plt.ylabel("Average Math Score")
plt.tight_layout()
plt.savefig("avg_math_borough.png")
plt.show()


# ## Schools with Above Average Total SAT Scores

# In[20]:


overall_avg_sat = schools['total_SAT'].mean()
above_avg_schools = schools[schools['total_SAT'] > overall_avg_sat]
print("\nSchools with Above Average SAT Scores:")
above_avg_schools[['school_name', 'total_SAT']].head(10)


# ## Correlation Between SAT Sections

# In[22]:


correlations = schools[['average_math', 'average_reading', 'average_writing']].corr()
print("\nCorrelation Between SAT Sections:")
correlations


# ## Visualization: Heatmap of SAT Section Correlations

# In[23]:


plt.figure(figsize=(8, 6))
sns.heatmap(correlations, annot=True, cmap="Blues", fmt=".2f")
plt.title("Correlation Between SAT Sections")
plt.tight_layout()
plt.savefig("sat_correlation.png")
plt.show()

