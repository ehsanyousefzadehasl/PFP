import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # set figure's size
    plt.figure(figsize=(10, 5))

    # dataset
    bars = ("w1", "w2", "w3", "w4", "w5", "w6", "w7", "w8", "w9")
    mechanism_1 = [0.8332, 0.5, 0.7032, 0.7072, 0.023, 1, 0.2261, 0.42, 0.8072]
    mechanism_2 = [0.7011, 0.5, 0.6714, 0.7051, 0.0194, 1, 0.181, 0.4198, 0.7635]
    mechanism_3 = [0.4958, 0.5, 0.5546, 0.7051, 0.018, 1, 0.0992, 0.4201, 0.7117]

    # set width of bar
    barWidth = 0.2

    # Set position of bar on X axis
    x1 = np.arange(len(bars))
    x2 = [x + barWidth for x in x1]
    x3 = [x + barWidth for x in x2]

    # Make the plot
    plt.bar(x1, [100 * i for i in mechanism_1], color='black', hatch="////", width=barWidth, edgecolor='white', label='mechanism 1')
    plt.bar(x2, [100 * i for i in mechanism_2], color='grey', hatch="....", width=barWidth, edgecolor='white', label='mechanism 2')
    plt.bar(x3, [100 * i for i in mechanism_3], color='blue', hatch="//////", width=barWidth, edgecolor='white', label='mechanism 3')

    # Add xticks on the middle of the group bars
    plt.xticks([r + barWidth for r in range(len(bars))], bars)

    plt.xlabel('Benchamrks', fontweight='bold')
    plt.ylabel('Parameter (%)', fontweight='bold')

    plt.legend(loc='center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)

    # Show graphic
    plt.savefig('./three_column_comparison_figure_plotter_output.pdf')
    plt.show()
