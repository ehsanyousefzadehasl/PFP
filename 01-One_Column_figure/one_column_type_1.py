import pandas as pd

import numpy as np
import matplotlib.pyplot as plt


def add_value_labels(ax, spacing=5):
    """Add labels to the end of each bar in a bar chart.

    Arguments:
        ax (matplotlib.axes.Axes): The matplotlib object containing the axes
            of the plot to annotate.
        spacing (int): The distance between the labels and the bars.
    """

    # For each bar: Place a label
    for rect in ax.patches:
        # Get X and Y placement of label from rect.
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2

        # Number of points between bar and label. Change to your liking.
        space = spacing
        # Vertical alignment for positive values
        va = 'bottom'

        # If value of bar is negative: Place label below bar
        if y_value < 0:
            # Invert space to place label below
            space *= -1
            # Vertically align label at top
            va = 'top'

        # Use Y value as label and format number with one decimal place
        label = "{:.2f}".format(y_value)

        # Create annotation
        ax.annotate(
            label,  # Use `label` as label
            (x_value, y_value),  # Place label at end of the bar
            xytext=(0, space),  # Vertically shift label by `space`
            textcoords="offset points",  # Interpret `xytext` as offset in points
            ha='center',  # Horizontally center label
            va=va)  # Vertically align label differently for
        # positive and negative values.


if __name__ == '__main__':
    # set figure's size
    plt.figure(figsize=(10, 6.5))

    # dataset
    bars = (
        'w1', 'w2', 'w3', 'w4', 'w5', 'w6', 'w7', 'w8', 'w9', 'w10', 'average')
    values = [4.5, 6.2, 8.3, 9.2, 10.2, 11.1, 12.8, 13.4, 16.23, 18.5, 15.1543]

    # set width of bar
    barWidth = 0.4

    freq_series = pd.Series(values)
    ax = freq_series.plot(kind='bar', width=barWidth)
    add_value_labels(ax)

    # Set position of bar on X axis
    x1 = np.arange(len(bars))

    # Make the plot
    plt.bar(x1, [i for i in values], color='black', hatch="////", width=barWidth, edgecolor='white', label='16k')

    # Add xticks on the middle of the group bars
    plt.xticks([r for r in range(len(bars))], bars, rotation=50)

    plt.xlabel('Benchmarks', fontweight='bold')
    plt.ylabel('Parameter to show (param unit)', fontweight='bold')

    # plt.legend(loc='center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)

    # Show graphic
    plt.savefig('./one_column_type1_output.pdf', bbox_inches='tight', pad_inches=.2)
    plt.show()
