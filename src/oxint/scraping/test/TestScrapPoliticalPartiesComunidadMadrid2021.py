import unittest

from oxint.scraping.ScrapPoliticalPartiesComunidadMadrid2021 import ScrapPoliticalPartiesComunidadMadrid2021


class TestScrapPoliticalPartiesComunidadMadrid2021(unittest.TestCase):

    URL_Cs = "https://elecciones.comunidad.madrid//es/formaciones-politicas/listado-candidaturas/ciudadanos-partido-ciudadania-cs"
    NAME_Cs = "CIUDADANOS-PARTIDO DE LA CIUDADANIA"
    PARTY_ABBREV_Cs = "Cs"

    def test_read(self):
        scrap = ScrapPoliticalPartiesComunidadMadrid2021()
        json_parties = scrap.read()
        print(json_parties)
        self.assertIsNotNone(json_parties)
        self.assertEqual(23, len(json_parties["elections"]["political_parties"]))

        self.assertEqual(self.URL_Cs, json_parties["elections"]["political_parties"][0]["candidates_url"])
        self.assertEqual(self.NAME_Cs, json_parties["elections"]["political_parties"][0]["party_name"])
        self.assertEqual(self.PARTY_ABBREV_Cs, json_parties["elections"]["political_parties"][0]["party_abbrev"])
