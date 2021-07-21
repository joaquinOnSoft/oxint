import unittest

from oxint.scraping.ScrapCandidatesMadrid2021 import ScrapCandidatesMadrid2021


class TestScrapCandidatesMadrid2021(unittest.TestCase):
    URL_CANDIDATES_PP = "https://elecciones.comunidad.madrid/es/formaciones-politicas/listado-candidaturas/" \
                        "partido-popular-pp"

    def test_read(self):
        scrap = ScrapCandidatesMadrid2021(self.URL_CANDIDATES_PP)
        json_candidates = scrap.read()
        self.assertIsNotNone(json_candidates)
        self.assertEqual(137, len(json_candidates["candidates"]))
        self.assertEqual("Isabel Natividad", json_candidates["candidates"][0]["first_name"])
        self.assertEqual("Díaz Ayuso", json_candidates["candidates"][0]["last_name"])
        self.assertEqual("Natalia", json_candidates["candidates"][136]["first_name"])
        self.assertEqual("Rey Riveiro", json_candidates["candidates"][136]["last_name"])


if __name__ == '__main__':
    unittest.main()
