ax = sns.scatterplot(x="total_bill", y="tip",
                     hue="day", style="time", data=tips)
