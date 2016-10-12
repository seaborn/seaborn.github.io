g = sns.FacetGrid(tips, col="day", size=4, aspect=.5)
g = g.map(sns.boxplot, "time", "total_bill")
