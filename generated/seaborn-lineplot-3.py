ax = sns.lineplot(x="timepoint", y="signal",
                  hue="event", style="event", data=fmri)
