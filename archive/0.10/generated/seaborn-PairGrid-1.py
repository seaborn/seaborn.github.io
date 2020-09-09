import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
iris = sns.load_dataset("iris")
g = sns.PairGrid(iris)
g = g.map(plt.scatter)
