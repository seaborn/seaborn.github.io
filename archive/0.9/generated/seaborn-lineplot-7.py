ax = sns.lineplot(x="timepoint", y="signal", hue="event",
                  units="subject", estimator=None, lw=1,
                  data=fmri.query("region == 'frontal'"))
