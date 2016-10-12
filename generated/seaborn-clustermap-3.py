cmap = sns.cubehelix_palette(as_cmap=True, rot=-.3, light=1)
g = sns.clustermap(flights, cmap=cmap, linewidths=.5)
