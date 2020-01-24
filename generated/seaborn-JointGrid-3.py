import matplotlib.pyplot as plt
g = sns.JointGrid(x="total_bill", y="tip", data=tips)
g = g.plot_joint(sns.scatterplot, color=".5")
g = g.plot_marginals(sns.distplot, kde=False, color=".5")
