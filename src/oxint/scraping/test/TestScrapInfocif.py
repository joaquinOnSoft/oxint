import unittest

from oxint.scraping.ScrapInfocif import ScrapInfocif


class TestScrapInfocif(unittest.TestCase):
    def test_search_company_by_cif(self):
        scraper = ScrapInfocif()
        company = scraper.search_company_by_cif("A28476208")

        self.assertIsNotNone(company)
        self.assertEqual(company['cif'], 'A28476208')
        self.assertEqual(company['num_employees'], '8.751')
        self.assertEqual(company['parent_company'], 'EMPRESA DE TRANSFORMACION AGRARIA SA SME MP')
        self.assertEqual(company['phone'], '-')
        self.assertEqual(company['register'], 'Registro Mercantil de Madrid')
        self.assertEqual(company['sector'], 'Equipos industriales')
        self.assertEqual(company['since'], '24/05/1977')
        self.assertEqual(company['state'], '-')
        self.assertEqual(company['web'], 'www.tragsa.es')
        self.assertEqual(company['address'], '')

        positions = company['positions']
        self.assertIsNotNone(positions)
        # self.assertEqual(3, len(positions))
        # self.assertEqual("CASAS GRANDE JESUS", positions[0]["name"])
        # self.assertEqual("8", positions[0]["linkages"])
        # self.assertEqual("RODRIGUEZ HERRER MARIA ELVIRA.Consj.Domini: MUÑOZ LOPEZ JOSE MIGUEL", positions[2]["name"])
        # self.assertEqual("1", positions[2]["linkages"])


if __name__ == '__main__':
    unittest.main()
