ax = sns.lineplot(x="time", y="firing_rate",
                  hue="coherence", style="choice",
                  palette="ch:2.5,.25", data=dots)
