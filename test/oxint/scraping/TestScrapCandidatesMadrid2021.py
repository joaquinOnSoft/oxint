import unittest

from oxint.scraping.ScrapCandidatesMadrid2021 import ScrapCandidatesMadrid2021


class TestScrapCandidatesMadrid2021(unittest.TestCase):
    URL_CANDIDATES_PP = "https://elecciones.comunidad.madrid/es/formaciones-politicas/listado-candidaturas/" \
                        "partido-popular-pp"

    def test_something(self):
        scrap = ScrapCandidatesMadrid2021(self.URL_CANDIDATES_PP)
        scrap.read()
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
