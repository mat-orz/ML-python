import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


penguins = pd.read_csv("data/penguins_classification.csv")

print(penguins.head())

numerical_columns = ['Culmen Length (mm)', 'Culmen Depth (mm)']

categorical_columns = ['Species']

print(penguins['Species'].value_counts())

hist = penguins.hist(figsize=(10, 5))

sns.pairplot(penguins, hue='Species')
plt.show()