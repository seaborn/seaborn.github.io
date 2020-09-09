ax = sns.lineplot(x="time", y="firing_rate",
                  size="coherence", hue="choice",
                  sizes=(.25, 2.5), data=dots)
