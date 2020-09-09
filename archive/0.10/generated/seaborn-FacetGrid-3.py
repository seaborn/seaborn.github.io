import numpy as np
bins = np.arange(0, 65, 5)
g = sns.FacetGrid(tips, col="time",  row="smoker")
g = g.map(plt.hist, "total_bill", bins=bins, color="r")
