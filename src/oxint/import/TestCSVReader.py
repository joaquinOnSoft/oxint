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
        self.assertEqual("Servicio de revisión de motor de las dresinas DT-301 a DT-304",
                         item0["OBJETO DEL CONTRATO"])

        # Check last row
        item54933 = content["items"][54933]
        self.assertEqual("Convocatoria anunciada a licitación", item54933["TIPO DE PUBLICACIÓN"])
        self.assertEqual("Referencia MI 305", item54933["Nº EXPEDIENTE"])
        self.assertEqual("116185", item54933["REFERENCIA"])
        self.assertEqual("", item54933["IMPORTE DE ADJUDICACIÓN(CON IVA)"])
        self.assertEqual("Equipamiento de señalización, ATP, ATO y CTC en la prolongación de la Línea 11 de Metro de "
                         "Madrid.  ", item54933["OBJETO DEL CONTRATO"])

    def test_ingest_with_custom_headers(self):
        custom_headers = [
            "publication_type",
            "contracting_entity",
            "file_no",
            "reference",
            "contract_object",
            "contract_type",
            "award_procedure",
            "bidding_budget_with_vat",
            "awardee_nif ",
            "awardee",
            "award_amount_with_vat"
        ]

        file_path = self.base_path + "resultados_contratos_comunidad_madrid.csv"
        reader = CSVReader()
        reader.custom_headers = custom_headers
        content = reader.ingest(file_path, 'ISO-8859-1', ';')

        self.assertIsNotNone(content)
        self.assertEqual(len(content["items"]), 54934)

        # Check first row
        item0 = content["items"][0]
        self.assertEqual("Convocatoria anunciada a licitación", item0["publication_type"])
        self.assertEqual("6012100216", item0["file_no"])
        self.assertEqual("4192659", item0["reference"])
        self.assertEqual("", item0["award_amount_with_vat"])
        self.assertEqual("Servicio de revisión de motor de las dresinas DT-301 a DT-304",
                         item0["contract_object"])

        # Check last row
        item54933 = content["items"][54933]
        self.assertEqual("Convocatoria anunciada a licitación", item54933["publication_type"])
        self.assertEqual("Referencia MI 305", item54933["file_no"])
        self.assertEqual("116185", item54933["reference"])
        self.assertEqual("", item54933["award_amount_with_vat"])
        self.assertEqual("Equipamiento de señalización, ATP, ATO y CTC en la prolongación de la Línea 11 de Metro de "
                         "Madrid.  ", item54933["contract_object"])


if __name__ == '__main__':
    unittest.main()
