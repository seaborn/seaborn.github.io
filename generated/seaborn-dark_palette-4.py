from numpy import arange
x = arange(25).reshape(5, 5)
cmap = sns.dark_palette("#2ecc71", as_cmap=True)
ax = sns.heatmap(x, cmap=cmap)
