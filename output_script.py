import pandas as pd
import matplotlib.pyplot as plt

file_location = open('uploaded_file_location.txt', 'r').readline().strip()
df = pd.read_csv(file_location)

df['SepalLengthCm'].hist()
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.savefig('sepal_length_distribution.png')