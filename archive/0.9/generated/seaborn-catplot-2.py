g = sns.catplot(x="time", y="pulse", hue="kind",
               data=exercise, kind="violin")
