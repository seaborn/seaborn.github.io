import pandas as pd
x, y = pd.Series(x, name="x_var"), pd.Series(y, name="y_var")
ax = sns.regplot(x=x, y=y, marker="+")
