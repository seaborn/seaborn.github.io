attend = sns.load_dataset("attention")
g = sns.FacetGrid(attend, col="subject", col_wrap=5,
                  size=1.5, ylim=(0, 10))
g = g.map(sns.pointplot, "solutions", "score", scale=.7)
