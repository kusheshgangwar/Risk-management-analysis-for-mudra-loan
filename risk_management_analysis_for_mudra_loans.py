# -*- coding: utf-8 -*-
"""Risk Management Analysis for MUDRA Loans.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16o3UlhBkNfwkqN6SlckZYcB1hY3LpEeg
"""

import pandas as pd
import numpy as np

data = pd.read_csv("/content/mudraloandataset.csv")

print(data)

data.info()

data.describe()

data.head()

data.tail()

data.duplicated().any()

df = data.drop_duplicates()

df.notnull()

df = pd.DataFrame({
    'A': [1, 2, None, 4, 5],
    'B': [10, None, 30, 40, 50]
})

# Replace NaN values with the mean of the column
df['A'] = df['A'].fillna(df['A'].mean())
df['B'] = df['B'].fillna(df['B'].mean())

print(df)

df['A'] = df['A'].fillna(df['A'].median())
df['B'] = df['B'].fillna(df['B'].median())

print(df)

df['A'] = df['A'].fillna(df['A'].mode()[0])  # mode() returns a Series, so we take the first value
df['B'] = df['B'].fillna(df['B'].mode()[0])
print(df)

df.quantile()

def replace_outliers_with_central_tendency(df, method='mean'):

    for col in df.select_dtypes(include=np.number).columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        if method == 'mean':
            central_tendency = df[col].mean()
        elif method == 'median':
            central_tendency = df[col].median()
        elif method == 'mode':
            central_tendency = df[col].mode()[0]
        else:
            raise ValueError("Invalid method. Choose 'mean', 'median', or 'mode'.")

        df[col] = np.where((df[col] < lower_bound) | (df[col] > upper_bound),
                           central_tendency, df[col])

    return df

# Example usage:
# Assuming you have your DataFrame 'df'

# Replace outliers with the mean
df_mean = replace_outliers_with_central_tendency(df.copy(), method='mean')

# Replace outliers with the median
df_median = replace_outliers_with_central_tendency(df.copy(), method='median')

# Replace outliers with the mode
df_mode = replace_outliers_with_central_tendency(df.copy(), method='mode')

print("Original DataFrame:\n", df)
print("\nDataFrame with outliers replaced by mean:\n", df_mean)
print("\nDataFrame with outliers replaced by median:\n", df_median)
print("\nDataFrame with outliers replaced by mode:\n", df_mode)

import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

plt.hist(df['A'], bins=10)
plt.xlabel('A')
plt.ylabel('Frequency')
plt.title('Histogram of A')
plt.show()

sns.boxplot(x=df['A'])
plt.title('Boxplot of A')
plt.show()

sns.kdeplot(df['A'])
plt.title('Density Plot of A')
plt.show()

categories = df['A'].unique()
counts = df['A'].value_counts()

plt.bar(categories, counts)
plt.xlabel('Categories')
plt.ylabel('Counts')
plt.title('Bar Plot of A')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

sns.violinplot(x=df['A'])
plt.title('Violin Plot of A')
plt.show()

data = df['A']
sm.qqplot(data, line='s')
plt.title('QQ Plot of A')
plt.show()

plt.scatter(df['A'], df['B'])
plt.xlabel('A')
plt.ylabel('B')
plt.title('Scatter Plot of A vs. B')
plt.show()

plt.plot(df['A'], df['B'])
plt.xlabel('A')
plt.ylabel('B')
plt.title('Line Plot of A vs. B')
plt.show()

correlation_matrix = df.corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Heatmap of Correlation Matrix')
plt.show()

sns.pairplot(df)
plt.show()

from google.colab import drive
drive.mount('/content/drive')

x = np.random.rand(50)
y = np.random.rand(50)
size = np.random.rand(50) * 100


plt.scatter(x, y, s=size, alpha=0.5)


plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Bubble Plot")

plt.show()

data = {'x_column': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'y_column': [2, 4, 1, 3, 5, 7, 6, 8, 9, 10]}
df = pd.DataFrame(data)

sns.jointplot(x='x_column', y='y_column', data=df, kind='reg')
plt.suptitle("Joint Plot of x_column vs. y_column", y=1.02)
plt.show()

x = np.random.rand(1000)
y = np.random.rand(1000)

plt.hexbin(x, y, gridsize=20, cmap='viridis')

plt.colorbar(label='Counts')

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Hexbin Plot")

plt.show()

categories = ['Category A', 'Category B', 'Category C']
values1 = [10, 15, 5]
values2 = [5, 10, 15]

plt.bar(categories, values1, label='Group 1')
plt.bar(categories, values2, bottom=values1, label='Group 2')

plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Stacked Bar Plot")
plt.legend()

plt.show()

