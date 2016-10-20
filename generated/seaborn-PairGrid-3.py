g = sns.PairGrid(iris, hue="species")
g = g.map(plt.scatter)
g = g.add_legend()
