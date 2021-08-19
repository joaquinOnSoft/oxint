from datetime import date
from datetime import datetime


class TimeUtils:

    @staticmethod
    def today() -> str:
        """
        Provides current day in format dd/mm/yyyy
        :return: current day in format dd/mm/yyyy
        SEE: https://www.programiz.com/python-programming/datetime/current-datetime
        """
        today = date.today()
        return today.strftime("%d/%m/%Y")

    @staticmethod
    def now() -> str:
        """
        Provides current day and time in format dd/MM/YYYY HH:mm:ss
        :return: current day and time in format dd/MM/YYYY HH:mm:ss
        SEE: https://www.programiz.com/python-programming/datetime/current-datetime
        """
        now = datetime.now()
        return now.strftime("%d/%m/%Y %H:%M:%S")
