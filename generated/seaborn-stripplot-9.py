ax =  sns.stripplot(x="day", y="total_bill", hue="smoker",
                   data=tips, palette="Set2", size=20, marker="D",
                   edgecolor="gray", alpha=.25)
