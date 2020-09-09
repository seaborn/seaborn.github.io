g = sns.relplot(x="total_bill", y="tip",
                 col="time", hue="day", style="day",
                 kind="scatter", data=tips)
