x, y = np.random.randn(2, 5000).cumsum(axis=1)
ax = sns.lineplot(x=x, y=y, sort=False, lw=1)
