ax = sns.regplot(x="x", y="y", data=ans.loc[ans.dataset == "III"],
                 scatter_kws={"s": 80},
                 robust=True, ci=None)
