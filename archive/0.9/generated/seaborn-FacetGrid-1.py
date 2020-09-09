import seaborn as sns; sns.set(style="ticks", color_codes=True)
tips = sns.load_dataset("tips")
g = sns.FacetGrid(tips, col="time", row="smoker")
