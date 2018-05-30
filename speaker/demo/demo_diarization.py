from speaker.model.speaker_diarization import speaker_diarization
from speaker.utils.utils import read_wav


def todiarize(input):
    fs, signal = read_wav(input)
    n, cls, sp = speaker_diarization(fs, signal)
    return {
        'filename': input,
        'nspeaker': n,
        'sp': sp
    }

