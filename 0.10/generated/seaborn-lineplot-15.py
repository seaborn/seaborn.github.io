list_data = [wide_df.loc[:"2005", "a"], wide_df.loc["2003":, "b"]]
ax = sns.lineplot(data=list_data)
