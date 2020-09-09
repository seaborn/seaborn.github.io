import seaborn as sns; sns.set(style="ticks", color_codes=True)
tips = sns.load_dataset("tips")
g = sns.JointGrid(x="total_bill", y="tip", data=tips)
