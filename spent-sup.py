import numpy as np
import matplotlib.pyplot as plt

np.read

# fake up some data
d1 = np.random.rand(1000)+5
d2 = np.append(np.random.rand(500)+4, np.random.rand(500)+6)

fig, ax = plt.subplots(figsize=(6,3))
labels = ["label 1", "label 2"]
plt1 = ax.violinplot([d1,d2])
plt.xticks([1, 2], labels)
plt.savefig("/home/dinosaur/testfig.png", format="png")