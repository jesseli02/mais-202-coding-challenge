import pandas as pd
import seaborn as sns

df = pd.read_csv(r'C:\Users\lijes\Projects\Python\Datasets\interest_rates\data.csv')

rates = df.groupby(df['purpose']).int_rate.mean()
rates = rates.reset_index()

ax = sns.barplot(x = 'purpose', y = 'int_rate', data = rates)
ax.set_xticklabels(ax.get_xticklabels(), rotation = 90)

print(rates.to_string(index = False))

