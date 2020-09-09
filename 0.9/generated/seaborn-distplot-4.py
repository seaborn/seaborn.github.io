from scipy.stats import norm
ax = sns.distplot(x, fit=norm, kde=False)
