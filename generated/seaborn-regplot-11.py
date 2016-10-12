ax = sns.regplot(x="size", y="total_bill", data=tips,
                 x_estimator=np.mean, logx=True, truncate=True)
