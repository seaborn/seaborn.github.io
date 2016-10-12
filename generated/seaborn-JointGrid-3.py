import matplotlib.pyplot as plt
g = sns.JointGrid(x="total_bill", y="tip", data=tips)
g = g.plot_joint(plt.scatter, color=".5", edgecolor="white")
g = g.plot_marginals(sns.distplot, kde=False, color=".5")
