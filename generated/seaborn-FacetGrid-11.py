attend = sns.load_dataset("attention")
g = sns.FacetGrid(attend, col="subject", col_wrap=5, size=1.5)
g = g.map(plt.plot, "solutions", "score", marker=".")
