import unittest

def run_all_tests():
    test_suite = unittest.TestSuite()

    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test_controller'))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test_plot'))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromName('test_configuration'))

    runner = unittest.TextTestRunner()
    runner.run(test_suite)

if __name__ == "__main__":
    run_all_tests()
