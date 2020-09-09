markers = {"Lunch": "s", "Dinner": "X"}
ax = sns.scatterplot(x="total_bill", y="tip", style="time",
                     markers=markers,
                     data=tips)
