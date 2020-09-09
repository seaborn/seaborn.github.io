g = sns.relplot(x="timepoint", y="signal",
                 col="region", hue="event", style="event",
                 kind="line", data=fmri)
