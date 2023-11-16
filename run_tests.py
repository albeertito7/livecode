from lib.TestRunner import TestRunner
from tests.TestSilence import TestSilence


tests_to_run = [TestSilence]

if __name__ == "__main__":
    runner = TestRunner(tests_to_run)
    runner.run()
