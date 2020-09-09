g = sns.relplot(x="total_bill", y="tip", hue="time",
                col="day", col_wrap=2, data=tips)
