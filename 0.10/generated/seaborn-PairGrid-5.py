g = sns.PairGrid(iris, vars=["sepal_length", "sepal_width"])
g = g.map(plt.scatter)
