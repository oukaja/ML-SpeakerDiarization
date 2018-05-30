"""
unit test
"""
import unittest
import os
import sys
sys.path.append('../')
from model.speaker_diarization import speaker_diarization
from utils.utils import read_wav


class TestFunc(unittest.TestCase):
    """
    Unit Test class
    """

    def test_speaker_diarization(self):
        """Test method speaker_diarization"""
        file_name = os.path.join(os.getcwd(), "data", "diarization", '3.wav')
        [fs, signal] = read_wav(file_name)
        self.assertEqual(int(os.path.basename(file_name)[:-4]), speaker_diarization(fs, signal))


if __name__ == '__main__':
    unittest.main()
