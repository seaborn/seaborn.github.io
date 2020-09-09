import seaborn as sns
sns.set(style="ticks")
tips = sns.load_dataset("tips")
g = sns.relplot(x="total_bill", y="tip", hue="day", data=tips)
