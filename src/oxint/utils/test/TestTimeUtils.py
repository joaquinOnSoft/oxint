import os
import unittest
from datetime import datetime, date
from unittest import TestCase

from oxint.utils.TimeUtils import TimeUtils


class TestTimeUtils(TestCase):

    def test_now(self):
        now = datetime.now()
        expect_now_str = now.strftime("%d/%m/%Y %H:%M:%S")
        self.assertEqual(expect_now_str, TimeUtils.now())

    def test_today(self):
        today = date.today()
        expected_today_str =  today.strftime("%d/%m/%Y")
        self.assertEqual(expected_today_str, TimeUtils.today())


if __name__ == '__main__':
    unittest.main()
