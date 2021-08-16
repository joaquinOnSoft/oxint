import unittest

# initialize the test suite
import oxint.ingest.TestCSVReader as TestCSVReader
import oxint.scraping.TestScrapCandidatesComunidadMadrid2021 as TestScrapCandidatesComunidadMadrid2021
import oxint.scraping.TestURLReader as TestURLReader
import oxint.utils.TestNameUtils as TestNameUtils
from oxint.scraping.TestScrapPoliticalPartiesComunidadMadrid2021 import TestScrapPoliticalPartiesComunidadMadrid2021

loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite

# oxint.ingest.TestCSVReader
suite.addTests(loader.loadTestsFromModule(TestCSVReader))

# oxint.scraping
suite.addTests(loader.loadTestsFromModule(TestScrapCandidatesComunidadMadrid2021))
suite.addTests(loader.loadTestsFromModule(TestScrapPoliticalPartiesComunidadMadrid2021))
suite.addTests(loader.loadTestsFromModule(TestURLReader))

# oxint.utils
suite.addTests(loader.loadTestsFromModule(TestNameUtils))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
