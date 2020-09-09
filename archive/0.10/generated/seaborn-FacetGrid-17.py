g = sns.FacetGrid(tips, col="smoker", row="sex",
                  margin_titles=True)
g = (g.map(plt.scatter, "total_bill", "tip", color="m", **kws)
      .set(xlim=(0, 60), ylim=(0, 12),
           xticks=[10, 30, 50], yticks=[2, 6, 10])
      .fig.subplots_adjust(wspace=.05, hspace=.05))
