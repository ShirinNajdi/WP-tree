"""
This repo will help researchers to explore sub-bands of wavelet packet decomposition and visualize them. 
This will lead to choose correct sub-bands for feature extraction.
"""
import itertools as it
import numpy as np
import matplotlib.pyplot as plt


def freq_band_name(level):
    """
    This function generates a list of the names of the subbands in wavelet packet decomposition.

    :param level: Wavelet packet decopmposition level.
    :return: List of the subband names where "a" refers to approximation and "d" refers to detail.
    """

    s = 'ad'
    permutations = it.product(s, repeat=level)
    freq_band_namelist = []
    for each in permutations:
        temp = ''.join(each)
        freq_band_namelist.append(temp)

    return freq_band_namelist


def freq_band_range(fs, level):
    """
    This function generates frequency intervals depending on the decomposition level and sampling frequency.

    :param fs: Sampling frequency of the signal.
    :param level: Wavelet packet decopmposition level.
    :return: List of frequency intervals in a specific level of wavelet packet decomposition.
    """

    fs = fs/2
    n = 2 ** level
    step = fs/n
    freq_band_list = [(round(step * i, 2), round(step * (i + 1), 2)) for i in range(n)]

    return freq_band_list


def main(fs, level):
    """

    :return: A dictionary of subband names and frequency intervals.
    """
    subband_list = []

    for cnt in range(1,level+1):

        name_list = freq_band_name(cnt)
        freq_band_list = freq_band_range(fs,cnt)
        freq_band_decomposition = dict(zip(name_list, freq_band_list))
        print(freq_band_decomposition)

        subband_list.append(freq_band_decomposition)

    # Plot wavelet packet tree
    y_step = 1/(level+1)
    y = np.arange(0, 1, y_step)[1:]
    plt.switch_backend('Qt4Agg')

    for cnt in range(1, level+1):

        data = subband_list[cnt-1]
        text = ['{} : {}'.format(key, value) for key, value in data.items()]
        y_temp = y[cnt-1]
        x_step = 1/(2**cnt+1)
        x_temp = np.arange(0, 1, x_step)[1:]

        for cnt1 in range(len(x_temp)):

            plt.text(x_temp[cnt1], y_temp, text[cnt1], size=10, rotation=90, ha="center", va="center")

    ax = plt.gca()

    # Remove white back ground
    ax.set_frame_on(False)

    # Remove axis and ticks
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # No padding
    plt.tight_layout(pad=0)

    # Maximize figure size
    fig = plt.get_current_fig_manager()
    fig.window.showMaximized()
    plt.show()


if __name__ == "__main__":
    main(200, 4)

