ax = sns.lineplot(x="timepoint", y="signal", hue="event",
                  err_style="bars", ci=68, data=fmri)
