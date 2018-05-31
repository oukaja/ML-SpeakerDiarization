from speaker.model.speaker_diarization import speaker_diarization
from speaker.utils.utils import read_wav


def todiarize(input):
    fs, signal = read_wav(input)
    n, cls, sp, z = speaker_diarization(fs, signal)
    return {
        'filename': z,
        'nspeaker': n,
        'sp': sp
    }


# if __name__=="__main__":
#    todiarize("C:\\Users\\OUKAJA\\Desktop\\oishi-master\\uploads\\1.wav")

