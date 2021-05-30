import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


adult_census = pd.read_csv("data/census.csv")

target_column = 'class'


print(adult_census[target_column].value_counts())

numerical_columns = [
    'age', 'education-num', 'capital-gain', 'capital-loss',
    'hours-per-week']

categorical_columns = [
    'workclass', 'education', 'marital-status', 'occupation',
    'relationship', 'race', 'sex', 'native-country']

all_columns = numerical_columns + categorical_columns + [target_column]

print('columns: ' + str(all_columns))
adult_census = adult_census[all_columns]

print(adult_census.head())
print(f"The dataset contains {adult_census.shape[0]} samples and "
      f"{adult_census.shape[1]} columns")
print(f"The dataset contains {adult_census.shape[1] - 1} features.")

print(adult_census['sex'].value_counts())
print(adult_census['education'].value_counts())

#hist = adult_census.hist(figsize=(10, 5))
#plt.show()

print(pd.crosstab(index=adult_census['education'],
            columns=adult_census['education-num']))

n_samples_to_plot = 5000
columns = ['age', 'education-num', 'hours-per-week']

ax = sns.scatterplot(
    x="age", y="hours-per-week", data=adult_census[:n_samples_to_plot],
    hue="class", alpha=0.5,
)

age_limit = 27
plt.axvline(x=age_limit, ymin=0, ymax=1, color="black", linestyle="--")

hours_per_week_limit = 40
plt.axhline(
    y=hours_per_week_limit, xmin=0.18, xmax=1, color="black", linestyle="--"
)

plt.annotate("<=50K", (17, 25), rotation=90, fontsize=35)
plt.annotate("<=50K", (35, 20), fontsize=35)
plt.annotate("???", (45, 60), fontsize=35)

plt.show()
plt.show()