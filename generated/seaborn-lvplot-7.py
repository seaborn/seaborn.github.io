ax = sns.lvplot(x="day", y="total_bill", data=tips)
ax = sns.stripplot(x="day", y="total_bill", data=tips,
                   size=4, jitter=True, color="gray")
