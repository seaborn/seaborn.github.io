from scipy import stats
def qqplot(x, y, **kwargs):
    _, xr = stats.probplot(x, fit=False)
    _, yr = stats.probplot(y, fit=False)
    plt.scatter(xr, yr, **kwargs)
g = sns.FacetGrid(tips, col="smoker", hue="sex")
g = (g.map(qqplot, "total_bill", "tip", **kws)
      .add_legend())
