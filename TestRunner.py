import unittest
import HtmlTestRunner
# import your test modules
from Tests import loginTest

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(loginTest))

# initialize a runner, pass it your suite and run it
runner = HtmlTestRunner.HTMLTestRunner(output='test-reports', verbosity=2)
runner.run(suite)
