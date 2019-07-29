# libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter


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
    # dataset
    ys = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.29, 0.34, 0.41, 0.61, 0.76]]

    for idx, y in enumerate(ys):
        # set figure's size
        plt.figure(figsize=(15, 7))

        bars = ['w1', 'w2', 'w3', 'w4', 'w5', 'w6', 'w7', 'w8', 'w9', 'w10', 'w11', 'w12', 'w13',
                'w14', 'w15', 'w16', 'w17', 'w18', 'w19', 'w20', 'w21', 'w22', 'w23']

        freq_series = pd.Series(y)
        ax = freq_series.plot(kind='bar')
        add_value_labels(ax)
        x = np.arange(len(bars))

        barWidth = 0.5

        plt.gca().yaxis.set_major_formatter(PercentFormatter(100))
        plt.bar(x, y, color='black', hatch="////", width=barWidth, edgecolor='white')

        plt.xticks(x, bars, rotation=50)

        plt.xlabel('Benchmarks', fontweight='bold')
        plt.ylabel('Parameter Value', fontweight='bold')

        plt.savefig('./one_column_type_3_output.png', bbox_inches='tight', pad_inches=.2)
        plt.show()
