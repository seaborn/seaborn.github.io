ax = sns.boxenplot(x="day", y="total_bill", hue="smoker",
                   data=tips, palette="Set3")
