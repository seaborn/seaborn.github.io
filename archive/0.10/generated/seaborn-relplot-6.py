fmri = sns.load_dataset("fmri")
g = sns.relplot(x="timepoint", y="signal",
                hue="event", style="event", col="region",
                kind="line", data=fmri)
