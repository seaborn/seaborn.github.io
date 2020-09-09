dots = sns.load_dataset("dots").query("align == 'dots'")
ax = sns.lineplot(x="time", y="firing_rate",
                  hue="coherence", style="choice",
                  data=dots)
