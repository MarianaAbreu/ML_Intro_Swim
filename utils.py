
import matplotlib.pyplot as plt
import seaborn as sns


def plot_one(data, column='Roll', sampling_rate=1000, save=True, show=True, figname='swimplot'):
    """
    Plot data from one column over time
    :param data: dataframe with a time column and other columns to use
    :param column: column to plot
    :param sampling_rate: sampling frequency to calculate time
    :param save: to save the figure in png
    :param show: to show the figure
    :return: None
    """
    sns.set()
    time = ((data['Time'] - data['Time'][0])/sampling_rate)
    fig = plt.figure(figsize=(20, 5))
    plt.plot(time, data[column], linewidth=4)
    plt.title('Swimming lap')
    plt.ylabel(column)
    plt.xlabel('Time (s)')
    if save:
        plt.savefig(figname + '.png', transparent=True)
    if show:
        plt.show()


def plot_all(data, column_list, together=True, sampling_rate=1000, save=True, show=True, figname='swimall'):
    """
    Plot several columns together indicated in column list
    :param data: input data to plot, must contain time column
    :param column_list: columns to plot in the Y axis
    :param together: if True, the plots will be overlayed, if False they will be separated
    :param sampling_rate: sampling frequency to compute time
    :param save: if True the plot will be saved in the directory
    :param show: if True the plot will be shown
    :param figname: name to save the figure under
    :return: None
    """
    sns.set()
    time = ((data['Time'] - data['Time'][0]) / sampling_rate)
    if together:
        plt.figure(figsize=(20, 5))
        for col in column_list:
            plt.plot(time, data[col], linewidth=4, label=col)
        plt.title('Swimming lap')
        plt.legend()
        plt.ylabel('Amplitude')
        plt.xlabel('Time (s)')
    else:
        plt.figure(figsize=(20, len(column_list)*4))
        plt.suptitle('Swimming lap')
        i = 1
        for col in column_list:
            plt.subplot(len(column_list), 1, i)
            plt.plot(time, data[col], linewidth=4, label=col)
            plt.ylabel(col)
            plt.xlabel('Time (s)')
            plt.legend()
            i += 1
    if save:
        plt.savefig(figname + '.png', transparent=True)
    if show:
        plt.show()

