tips["weekend"] = tips["day"].isin(["Sat", "Sun"])
ax = sns.violinplot(x="day", y="total_bill", hue="weekend",
                    data=tips, dodge=False)
