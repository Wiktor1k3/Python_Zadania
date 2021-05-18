import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("iris.csv", names=["sepal len", "sepal wid", "petal len", "petal wid", "class"])
df = pd.DataFrame(df)
df = df[["sepal len", "sepal wid", "class"]]
plt.xlabel("sepal length")
plt.ylabel("sepal width")
plt.title("Iris sepal length and width")
plt.show()