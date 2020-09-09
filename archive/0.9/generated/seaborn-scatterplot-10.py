cmap = sns.cubehelix_palette(dark=.3, light=.8, as_cmap=True)
ax = sns.scatterplot(x="total_bill", y="tip",
                     hue="day", size="smoker",
                     palette="Set2",
                     data=tips)
