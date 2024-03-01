import pandas as pd
import matplotlib.pyplot as plt

file_location = open('uploaded_file_location.txt', 'r').readline().strip()
df = pd.read_csv(file_location)

plt.figure(figsize=(8,8))
df['Species'].value_counts().plot.pie(autopct='%1.1f%%')
plt.ylabel('')
plt.title('Pie Chart of Species')
plt.savefig('pie_chart_species.png')