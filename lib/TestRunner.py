import unittest

from lib.Singleton import Singleton


class TestRunner(Singleton):
    def __init__(
        self, tests_to_run, runner=unittest.TextTestRunner(), suite=unittest.TestSuite()
    ):
        self.tests_to_run = tests_to_run
        self.runner = runner
        self.suite = suite

    def createSuite(self):
        loader = unittest.TestLoader()
        suites_list = []

        for test_class in self.tests_to_run:
            suite = loader.loadTestsFromTestCase(test_class)
            suites_list.append(suite)

        return unittest.TestSuite(suites_list)

    def run(self):
        self.runner.run(self.createSuite())
