import pandas as pd
import matplotlib.pyplot as plt

file_location = open('uploaded_file_location.txt', 'r').readline().strip()
df = pd.read_csv(file_location)

plt.hist(df['SepalWidthCm'])
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.title('Distribution of Sepal Width')
plt.savefig('sepal_width_distribution.png')