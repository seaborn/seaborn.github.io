cmap = sns.cubehelix_palette(dark=0, light=1, as_cmap=True)
ax = sns.heatmap(x, cmap=cmap)
