g = sns.FacetGrid(tips, col="smoker", row="sex")
g = (g.map(plt.scatter, "total_bill", "tip", color="g", **kws)
      .set_axis_labels("Total bill (US Dollars)", "Tip"))
