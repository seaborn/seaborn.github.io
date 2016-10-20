g = sns.PairGrid(iris,
                 x_vars=["sepal_length", "sepal_width"],
                 y_vars=["petal_length", "petal_width"])
g = g.map(plt.scatter)
