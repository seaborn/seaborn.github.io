g = sns.relplot(x="total_bill", y="tip", hue="day",
                col="time", row="sex", data=tips)
