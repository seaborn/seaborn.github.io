import numpy as np
g = sns.JointGrid(x="total_bill", y="tip", data=tips)
g = g.plot_joint(plt.scatter, color="m", edgecolor="white")
_ = g.ax_marg_x.hist(tips["total_bill"], color="b", alpha=.6,
                     bins=np.arange(0, 60, 5))
_ = g.ax_marg_y.hist(tips["tip"], color="r", alpha=.6,
                     orientation="horizontal",
                     bins=np.arange(0, 12, 1))
