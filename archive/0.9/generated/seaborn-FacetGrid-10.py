g = sns.FacetGrid(tips, col="sex", hue="time", palette=pal,
                  hue_order=["Dinner", "Lunch"],
                  hue_kws=dict(marker=["^", "v"]))
g = (g.map(plt.scatter, "total_bill", "tip", **kws)
     .add_legend())
