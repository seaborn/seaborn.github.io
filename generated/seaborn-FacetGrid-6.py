g = sns.FacetGrid(tips, col="day", size=4, aspect=.5)
g = g.map(plt.hist, "total_bill", bins=bins)
