g = sns.PairGrid(iris, hue="species", palette="Set2",
                 hue_kws={"marker": ["o", "s", "D"]})
g = g.map(plt.scatter, linewidths=1, edgecolor="w", s=40)
g = g.add_legend()
