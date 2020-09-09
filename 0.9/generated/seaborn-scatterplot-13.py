iris = sns.load_dataset("iris")
ax = sns.scatterplot(x=iris.sepal_length, y=iris.sepal_width,
                     hue=iris.species, style=iris.species)
