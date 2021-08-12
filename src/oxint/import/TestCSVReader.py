import os
import unittest

from CSVReader import CSVReader


class TestCSVReader(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.base_path = os.path.dirname(os.path.realpath(__file__))
        self.base_path += "/../../../resources/"

    def test_ingest(self):
        file_path = self.base_path + "resultados_contratos_comunidad_madrid.csv"
        reader = CSVReader()
        content = reader.ingest(file_path, 'ISO-8859-1', ';')
        self.assertIsNotNone(content)
        self.assertEqual(len(content["items"]), 54934)

        # Check first row
        item0 = content["items"][0]
        self.assertEqual("Convocatoria anunciada a licitación", item0["TIPO DE PUBLICACIÓN"])
        self.assertEqual("6012100216", item0["Nº EXPEDIENTE"])
        self.assertEqual("4192659", item0["REFERENCIA"])
        self.assertEqual("", item0["IMPORTE DE ADJUDICACIÓN(CON IVA)"])

        # Check last row
        item54933 = content["items"][54933]
        self.assertEqual("Convocatoria anunciada a licitación", item54933["TIPO DE PUBLICACIÓN"])
        self.assertEqual("Referencia MI 305", item54933["Nº EXPEDIENTE"])
        self.assertEqual("116185", item54933["REFERENCIA"])
        self.assertEqual("", item54933["IMPORTE DE ADJUDICACIÓN(CON IVA)"])


if __name__ == '__main__':
    unittest.main()
