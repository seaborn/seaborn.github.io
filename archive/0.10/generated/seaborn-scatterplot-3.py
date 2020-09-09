ax = sns.scatterplot(x="total_bill", y="tip",
                     hue="time", style="time", data=tips)
