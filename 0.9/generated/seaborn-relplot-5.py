g = sns.relplot(x="total_bill", y="tip", hue="time", size="size",
                palette=["b", "r"], sizes=(10, 100),
                col="time", data=tips)
