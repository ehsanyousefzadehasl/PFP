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
    plt.figure(figsize=(15, 5))

    # dataset
    bars = (
        'w1', 'w2', 'w3', 'w4', 'w5', 'w6', 'w7', 'w8', 'w9', 'w10', 'w11', 'w12',
        'Gmean')
    baseline = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    proposed = [1.09, 1.21, 1.32, 1.35, 1.38, 1.39, 1.51, 1.589, 1.62, 1.63, 1.71, 1.74, 1.35]

    # set width of bar
    barWidth = 0.3

    # Set position of bar on X axis
    x1 = np.arange(len(bars))
    x2 = [x + barWidth for x in x1]

    # Make the plot
    plt.bar(x1, [i for i in baseline], color='black', hatch="////", width=barWidth, edgecolor='white', label='Baseline')
    plt.bar(x2, [i for i in proposed], color='navy', hatch="....", width=barWidth, edgecolor='white',
            label='proposed')

    # Add xticks on the middle of the group bars
    plt.xticks([r + barWidth / 2 for r in range(len(bars))], bars)

    plt.xlabel('Becnhmarks', fontweight='bold')
    plt.ylabel('Comparison Metric', fontweight='bold')

    plt.legend(loc='center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)

    # Show graphic
    plt.savefig('./two_column_comparison_figure_output.pdf', bbox_inches='tight',
                pad_inches=.2)
    plt.show()
