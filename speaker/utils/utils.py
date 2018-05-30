"""
Fonctions utils couramment utilisées
"""
import operator
from scipy.io import wavfile
import numpy
from sklearn.mixture import GaussianMixture
EPS = numpy.finfo(float).eps


def read_wav(fname):
    """
    wav
    :param fname:
    :return: fs, signal
    """
    fs, signal = wavfile.read(fname)
    assert len(signal.shape) == 1, "Only Support Mono Wav File!"
    return fs, signal


def write_wav(fname, fs, signal):
    """
    wav
    """
    assert len(signal.shape) == 1, "Only Support Mono Wav File!"
    wavfile.write(fname, fs, signal)


def normalize_features(features):
    """
    :param features:
    :return: features_norm, mean_features, std_features
    """
    all_features = numpy.array([])
    count = 0
    for feature in features:
        if feature.shape[0] > 0:
            if count == 0:
                all_features = feature
            else:
                all_features = numpy.vstack((all_features, feature))
            count += 1

    mean_features = numpy.mean(all_features, axis=0) + EPS
    std_features = numpy.std(all_features, axis=0) + EPS

    features_norm = []
    for feature in features:
        feat_tmp = feature.copy()
        for n_samples in range(feature.shape[0]):
            feat_tmp[n_samples, :] = (feat_tmp[n_samples, :] - mean_features) / std_features
        features_norm.append(feat_tmp)
    return (features_norm, mean_features, std_features)
