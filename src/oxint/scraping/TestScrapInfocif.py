import unittest

from oxint.scraping.ScrapInfocif import ScrapInfocif


class TestScrapInfocif(unittest.TestCase):
    def test_search_company_by_cif(self):
        scraper = ScrapInfocif()
        company = scraper.search_company_by_cif("A28476208")

        self.assertIsNotNone(company)
        self.assertEqual(company['cif'], 'A28476208')
        self.assertEqual(company['num_employees'], '6.851')
        self.assertEqual(company['parent_company'], 'EMPRESA DE TRANSFORMACION AGRARIA SA SME MP')
        self.assertEqual(company['phone'], '914010774')
        self.assertEqual(company['register'], 'Registro Mercantil de Madrid')
        self.assertEqual(company['sector'], 'EQUIPOS INDUSTRIALES')
        self.assertEqual(company['since'], '24/05/1977')
        self.assertEqual(company['state'], '-')
        self.assertEqual(company['web'], 'www.tragsa.es')
        self.assertEqual(company['address'], 'Calle Maldonado, 58 28006 - Madrid')


if __name__ == '__main__':
    unittest.main()
