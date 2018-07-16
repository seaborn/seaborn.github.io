from matplotlib.colors import LogNorm
ax = sns.lineplot(x="time", y="firing_rate",
                  hue="coherence", style="choice",
                  hue_norm=LogNorm(), data=dots)
