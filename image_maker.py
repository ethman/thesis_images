import matplotlib.pyplot as plt
import numpy as np
import scipy.signal
import nussl
import librosa
import librosa.display
from nussl.core import utils
import os


def _get_signal(with_stems=False, track='Track00001'):
    babyslakh = os.path.expanduser('~/Documents/School/Research/babyslakh_16k')
    track = os.path.join(babyslakh, track)
    mix = nussl.AudioSignal(os.path.join(track, 'mix.wav'))
    if not with_stems:
        return mix

    stem_names = os.listdir(os.path.join(babyslakh, track, 'stems'))
    stems = {}
    for s in stem_names:
        if os.path.splitext(s)[1] == '.wav':
            stem_path = os.path.join(babyslakh, track, 'stems', s)
            stems[os.path.splitext(s)[0]] = nussl.AudioSignal(stem_path)

    return  mix, stems

def _display_spec(signal, ax):
    spec = librosa.amplitude_to_db(np.abs(signal.stft()), ref=np.max)
    librosa.display.specshow(spec, y_axis='log', sr=signal.sample_rate,
                             x_axis='time', ax=ax)


def plot_mix_and_stems():
    mix, stems = _get_signal(with_stems=True)

    n_plots = len(stems) + 1

    fig, axes = plt.subplot(n_rows=n_plots, figsize=(10, n_plots * 5),
                            sharex=True)
    _display_spec(mix, axes[0])
    axes[0].set_title('Mix')

    for i, st in enumerate(stems):
        _display_spec(st, axes[0])
        axes[i+1].set_title(f'Stem {i}: {st.label}')

    fig.show()



def plot_masks():
    mix, stems = _get_signal(with_stems=True)
    i = 0


def main():
    plot_mix_and_stems()


if __name__ == '__main__':
    main()