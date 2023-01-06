import os
import unittest
from unittest import TestCase

from oxint.utils.URLUtils import URLUtils


class TestURLUtils(TestCase):

    def setUp(self) -> None:
        super().setUp()
        # self.base_path = os.path.dirname(os.path.realpath(__file__))
        # self.base_path += "/../../../resources/"

    def test_get_html_from_url(self):
        # path = self.base_path + "test.html"
        # self.assertTrue(URLUtils.is_html(path))
        html = URLUtils.get_html_from_url("http://www.infocif.es/general/empresas-informacion-listado-empresas.asp"
                                          "?Buscar=A28476208")
        # print(html)
        self.assertIsNotNone(html)


if __name__ == '__main__':
    unittest.main()
