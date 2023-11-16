import unittest
from src.silence import silence_is_golden


class TestSilence(unittest.TestCase):
    def test_silence(self):
        self.assertEqual("Silence is golden", silence_is_golden())
