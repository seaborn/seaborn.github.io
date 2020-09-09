ax = sns.lineplot(x="timepoint", y="signal",
                  hue="region", style="event", data=fmri)
