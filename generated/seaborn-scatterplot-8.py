cmap = sns.cubehelix_palette(dark=.3, light=.8, as_cmap=True)
ax = sns.scatterplot(x="total_bill", y="tip",
                     hue="size", size="size",
                     sizes=(20, 200), palette=cmap,
                     legend="full", data=tips)
