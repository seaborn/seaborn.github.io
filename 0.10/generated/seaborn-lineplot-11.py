palette = sns.color_palette("mako_r", 6)
ax = sns.lineplot(x="time", y="firing_rate",
                  hue="coherence", style="choice",
                  palette=palette, data=dots)
