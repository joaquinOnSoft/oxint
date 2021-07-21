import unittest

from oxint.utils.NameUtils import NameUtils


class TestNameUtils(unittest.TestCase):
    def test_get_first_name_from_full_name(self):
        name = NameUtils.get_first_name_from_full_name("Isabel Natividad Díaz Ayuso")
        self.assertEqual("Isabel Natividad", name)

        name = NameUtils.get_first_name_from_full_name("Enrique Ruiz Escudero")
        self.assertEqual("Enrique", name)

        name = NameUtils.get_first_name_from_full_name("Alfonso Carlos Serrano Sánchez-Capuchino")
        self.assertEqual("Alfonso Carlos", name)

    def test_get_last_name_from_full_name(self):
        name = NameUtils.get_last_name_from_full_name("Isabel Natividad Díaz Ayuso")
        self.assertEqual("Díaz Ayuso", name)

        name = NameUtils.get_last_name_from_full_name("Enrique Ruiz Escudero")
        self.assertEqual("Ruiz Escudero", name)

        name = NameUtils.get_last_name_from_full_name("Alfonso Carlos Serrano Sánchez-Capuchino")
        self.assertEqual("Serrano Sánchez-Capuchino", name)


if __name__ == '__main__':
    unittest.main()
