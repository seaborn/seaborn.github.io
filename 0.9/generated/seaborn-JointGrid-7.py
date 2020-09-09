g = sns.JointGrid(x="total_bill", y="tip", data=tips, space=0)
g = g.plot_joint(sns.kdeplot, cmap="Blues_d")
g = g.plot_marginals(sns.kdeplot, shade=True)
