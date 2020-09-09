ax = sns.lineplot(x="time", y="firing_rate",
                  size="coherence", hue="choice",
                  legend="full", data=dots)
