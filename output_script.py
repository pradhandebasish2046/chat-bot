import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_location = open('uploaded_file_location.txt', 'r').readline().strip()
df = pd.read_csv(file_location)

df_numeric = df.select_dtypes(include=['int64', 'float64'])
sns.heatmap(df_numeric.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Plot')
plt.savefig('correlation_plot.png')