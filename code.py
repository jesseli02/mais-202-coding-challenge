import pandas as pd
import seaborn as sns

#read csv file
url = 'https://raw.githubusercontent.com/McGillAISociety/mais-202-coding-challenge/master/data.csv'
df = pd.read_csv(url)

#create new dataframe with mean of each purpose
rates = df.groupby(df['purpose']).int_rate.mean()
rates = rates.reset_index()

#plot bar graph
ax = sns.barplot(x = 'purpose', y = 'int_rate', data = rates)
ax.set_xticklabels(ax.get_xticklabels(), rotation = 90)

#print dataframe table
print(rates.to_string(index = False))

