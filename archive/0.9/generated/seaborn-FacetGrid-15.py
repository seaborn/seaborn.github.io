g = sns.FacetGrid(tips, col="smoker", row="sex")
g = (g.map(plt.scatter, "total_bill", "tip", color="r", **kws)
      .set(xlim=(0, 60), ylim=(0, 12),
           xticks=[10, 30, 50], yticks=[2, 6, 10]))
