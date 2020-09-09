ans = sns.load_dataset("anscombe")
ax = sns.regplot(x="x", y="y", data=ans.loc[ans.dataset == "II"],
                 scatter_kws={"s": 80},
                 order=2, ci=None, truncate=True)
