from cProfile import label
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import data
data = pd.read_csv("spent-supernatant-data.csv", index_col=0)
data = data[data["Condition"]!="50% Unfiltered"]
group = data.drop("Image", axis=1).groupby(["Condition", "Well"], sort=False)
group_all = data.drop(["Image", "Well"], axis=1).groupby(["Condition"], sort=False)

# Find variance within wells and within conditions


# Calculate average, stdev for Yeast, Intermediate, Hyphae 

# Do statistical test for differences between conditions

# Plot averages

means = group_all.mean()
stdevs = group_all.std()

axes = means.plot.bar(subplots=True,figsize=(12,8))
for ax in axes:
    ax.get_legend().remove()
plt.subplots_adjust(left=0.1,
                    bottom=0.2, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)
plt.savefig("prelim-fig.png", type="png")



fig = plt.figure(figsize=(8,6))
ax = plt.axes()
ax.set_yscale('log')

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

boxes = []
labels = []
i = 1
colors = ["tab:blue", "tab:orange", "tab:green"]
for g in group_all:
    labels.append(g[0])
    sub_df = g[1].drop("Condition",axis=1)
    bp = plt.boxplot(sub_df.T, positions = [i, i+1, i+2], widths = 0.6, patch_artist=True)
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
    i+=3
plt.xticks(range(2, len(labels) * 3 + 2, 3), labels)
plt.legend(["Yeast", "Hyphae", "Intermediate"], label_color = colors)

data_a = [[1,2,5], [5,7,2,2,5], [7,2,5]]
data_b = [[6,4,2], [1,2,5,3,2], [2,3,5,1]]

ticks = ['A', 'B', 'C']

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

plt.figure()

bpl = plt.boxplot(data_a, positions=np.array(xrange(len(data_a)))*2.0-0.4, sym='', widths=0.6)
bpr = plt.boxplot(data_b, positions=np.array(xrange(len(data_b)))*2.0+0.4, sym='', widths=0.6)
set_box_color(bpl, '#D7191C') # colors are from http://colorbrewer2.org/
set_box_color(bpr, '#2C7BB6')

# draw temporary red and blue lines and use them to create a legend
plt.plot([], c='#D7191C', label='Apples')
plt.plot([], c='#2C7BB6', label='Oranges')
plt.legend()

plt.xticks(xrange(0, len(ticks) * 2, 2), ticks)
plt.xlim(-2, len(ticks)*2)
plt.ylim(0, 8)
plt.tight_layout()
plt.savefig('boxcompare.png')