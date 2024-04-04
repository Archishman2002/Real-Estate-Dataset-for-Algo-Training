import pandas as pd

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

path="/content/drive/MyDrive/Real estate valuation data set.csv"
df = pd.read_csv(path)
df.describe

df = df.loc[:, (df != 0).any(axis=0)]
df.describe

df.head

df.shape
df.dtypes
df.describe()

df.isnull().sum()
df.dropna(inplace=True)
df

numerical_columns = df.select_dtypes(include="number").columns

pie_column = numerical_columns[5] # or any other column you want
pie_df = df.groupby(pie_column).sum()
pie_labels = pie_df.index
pie_values = pie_df.iloc[:, 5] # or any other column you want
plt.pie(pie_values, labels=pie_labels, autopct="%1.1f%%")
plt.title(f"Pie chart for {pie_column}")
plt.show()

bar_column_x = numerical_columns[3] # or any other column you want
bar_column_y = numerical_columns[2] # or any other column you want
bar_data = df[[bar_column_x, bar_column_y]]
sns.barplot(x=bar_column_x, y=bar_column_y, data=bar_data)
plt.title(f"Bar graph for {bar_column_x} and {bar_column_y}")
plt.show()

line_column = numerical_columns[3] # or any other column you want
line_data = df[line_column]
plt.plot(line_data)
plt.title(f"Line plot for {line_column}")
plt.show()

scatter_column_x = numerical_columns[2] # or any other column you want
scatter_column_y = numerical_columns[4] # or any other column you want
scatter_data = df[[scatter_column_x, scatter_column_y]]
plt.scatter(x=scatter_column_x, y=scatter_column_y, data=scatter_data)
plt.title(f"Scatter plot for {scatter_column_x} and {scatter_column_y}")
plt.show()

hist_column = numerical_columns[5] # or any other column you want
hist_data = df[hist_column]
plt.hist(hist_data)
plt.title(f"Histogram for {hist_column}")
plt.show()

heatmap_data = df[numerical_columns].corr()
sns.heatmap(heatmap_data, annot=True)
plt.title("Heatmap for the correlation matrix of the numerical columns")
plt.show()

summary = f"The heatmap shows the correlation matrix of the {len(numerical_columns)} numerical columns in the data. The correlation matrix is a table that shows the correlation coefficients between each pair of numerical columns. The correlation coefficient is a measure of how closely two variables are related to each other. It ranges from -1 to 1, where -1 means a perfect negative correlation, 0 means no correlation, and 1 means a perfect positive correlation. The heatmap uses a color scale to indicate the strength and direction of the correlation. The darker the color, the stronger the correlation. The colors on the diagonal represent the correlation of each column with itself, which is always 1.\n\n"

upper_triangle = heatmap_data.where(np.triu(np.ones(heatmap_data.shape), k=1).astype(np.bool))
max_corr = upper_triangle.max().max()
min_corr = upper_triangle.min().min()
max_pairs = list(zip(*np.where(upper_triangle == max_corr)))
min_pairs = list(zip(*np.where(upper_triangle == min_corr)))
max_columns = [(numerical_columns[x], numerical_columns[y]) for (x, y) in max_pairs]
min_columns = [(numerical_columns[x], numerical_columns[y]) for (x, y) in min_pairs]

def format_pairs(pairs):
  if len(pairs) == 1:
    return f"{pairs[0][0]} and {pairs[0][1]}"
  elif len(pairs) == 2:
    return f"{pairs[0][0]} and {pairs[0][1]}, and {pairs[1][0]} and {pairs[1][1]}"
  else:
    return ", ".join([f"{x} and {y}" for (x, y) in pairs[:-1]]) + f", and {pairs[-1][0]} and {pairs[-1][1]}"

summary += f"The most correlated pairs of columns are {format_pairs(max_columns)}, with a correlation coefficient of {max_corr:.2f}. This means that these pairs of columns have a strong positive relationship, and they tend to increase or decrease together. The least correlated pairs of columns are {format_pairs(min_columns)}, with a correlation coefficient of {min_corr:.2f}. This means that these pairs of columns have a strong negative relationship, and they tend to move in opposite directions.\n\n"
print(summary)

#END OF CODE
#COPY MAT KARNA NA PLEASE, UMMMM...... NHI NHI COPY KARLENA PAR EK BAAR BATA DENA CONNECT KARKE IF YOU WISH TO PLEASE PLEASE, THIS IS THE LEAST I CAN EXPECT!
