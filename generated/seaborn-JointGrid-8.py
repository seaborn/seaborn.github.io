g = sns.JointGrid(x="total_bill", y="tip", data=tips,
                  size=5, ratio=2)
g = g.plot_joint(sns.kdeplot, cmap="Reds_d")
g = g.plot_marginals(sns.kdeplot, color="r", shade=True)
