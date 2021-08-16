ax = sns.boxenplot(x="day", y="total_bill", hue="time",
                   data=tips, linewidth=2.5)
