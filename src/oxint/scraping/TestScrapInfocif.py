import unittest

from oxint.scraping.ScrapInfocif import ScrapInfocif


class TestScrapInfocif(unittest.TestCase):
    def test_search_company_by_cif(self):
        scraper = ScrapInfocif()
        json = scraper.search_company_by_cif("A28476208")
        print(json)
        self.assertIsNotNone(json)
        self.assertEqual("", json)  # add assertion here


if __name__ == '__main__':
    unittest.main()
