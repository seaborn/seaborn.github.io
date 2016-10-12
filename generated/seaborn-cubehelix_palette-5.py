from numpy import arange
x = arange(25).reshape(5, 5)
cmap = sns.cubehelix_palette(as_cmap=True)
ax = sns.heatmap(x, cmap=cmap)
