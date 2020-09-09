g = sns.JointGrid(x="total_bill", y="tip", data=tips)
g = g.plot_joint(plt.scatter,
                 color="g", s=40, edgecolor="white")
g = g.plot_marginals(sns.distplot, kde=False, color="g")
rsquare = lambda a, b: stats.pearsonr(a, b)[0] ** 2
g = g.annotate(rsquare, template="{stat}: {val:.2f}",
               stat="$R^2$", loc="upper left", fontsize=12)
