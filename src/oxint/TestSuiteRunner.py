import unittest

# initialize the test suite
import oxint.scraping.TestScrapCandidatesComunidadMadrid2021 as TestScrapCandidatesComunidadMadrid2021
import oxint.scraping.TestURLReader as TestURLReader
import oxint.utils.TestNameUtils as TestNameUtils

loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(TestScrapCandidatesComunidadMadrid2021))
suite.addTests(loader.loadTestsFromModule(TestURLReader))
suite.addTests(loader.loadTestsFromModule(TestNameUtils))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
