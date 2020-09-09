g = sns.clustermap(iris,
                   figsize=(7, 5),
                   row_cluster=False,
                   dendrogram_ratio=(.1, .2),
                   cbar_pos=(0, .2, .03, .4))
