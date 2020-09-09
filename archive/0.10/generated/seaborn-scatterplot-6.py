ax = sns.scatterplot(x="total_bill", y="tip",
                     hue="size", size="size",
                     data=tips)
