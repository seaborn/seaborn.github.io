g = sns.relplot(x="timepoint", y="signal",
                hue="event", style="event", col="region",
                height=5, aspect=.7, kind="line", data=fmri)
