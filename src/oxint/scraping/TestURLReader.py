import unittest

from oxint.scraping.URLReader import URLReader


class TestURLReader(unittest.TestCase):
    URL_CANDIDATES_PP_MADRID_2021 = "https://elecciones.comunidad.madrid/es/formaciones-politicas/listado-candidaturas/" \
                        "partido-popular-pp "

    def test_read(self):
        reader = URLReader(self.URL_CANDIDATES_PP_MADRID_2021)
        html = reader.read()
        self.assertIsNotNone(html)
        self.assertTrue(html.find("Isabel Natividad Díaz Ayuso"))


if __name__ == '__main__':
    unittest.main()
