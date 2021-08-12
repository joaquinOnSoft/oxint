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
        content = CSVReader.ingest(file_path, 'ISO-8859-1', ';')
        self.assertIsNotNone(content)
        self.assertEqual(len(content["items"]), 54934)


if __name__ == '__main__':
    unittest.main()
