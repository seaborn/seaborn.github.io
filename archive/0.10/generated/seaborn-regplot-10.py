tips["big_tip"] = (tips.tip / tips.total_bill) > .175
ax = sns.regplot(x="total_bill", y="big_tip", data=tips,
                 logistic=True, n_boot=500, y_jitter=.03)
