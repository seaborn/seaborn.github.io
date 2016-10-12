g = sns.JointGrid(x="total_bill", y="tip", data=tips,
                  xlim=(0, 50), ylim=(0, 8))
g = g.plot_joint(sns.kdeplot, cmap="Purples_d")
g = g.plot_marginals(sns.kdeplot, color="m", shade=True)
