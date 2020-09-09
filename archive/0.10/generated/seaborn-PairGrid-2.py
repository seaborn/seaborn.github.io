g = sns.PairGrid(iris)
g = g.map_diag(plt.hist)
g = g.map_offdiag(plt.scatter)
