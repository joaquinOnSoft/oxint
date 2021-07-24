import logging
import re

from oxint.scraping.URLReader import URLReader
from oxint.utils.NameUtils import NameUtils


class ScrapPoliticalPartiesComunidadMadrid2021(URLReader):
    """
    Recover the list of political parties that has participated
    in the "Comunidad de Madrid" elections in 2021.
    https://elecciones.comunidad.madrid/es/formaciones-politicas/listado-candidaturas-proclamadas
    """

    URL_BASE_MADRID_ELECTIONS = "https://elecciones.comunidad.madrid/"
    URL_CANDIDATURES_MADRID_2021 = URL_BASE_MADRID_ELECTIONS + "/es/formaciones-politicas/" \
                                                               "listado-candidaturas-proclamadas"

    def __init__(self):
        super().__init__(self.URL_CANDIDATURES_MADRID_2021)

    def read(self):
        """
        Recover the list of political parties for the Comunidad de Madrid 2021
        :return: JSON object that includes the first name, last name and
        political party abbreviation for each candidate
        """
        html = super().read()

        parties = re.findall(r"<a href=\"(.*)\" hreflang=\"es\">(.*)<\/a>", html)
        return self.__political_parties_to_json(parties)

    def __political_parties_to_json(self, parties: str):
        json_parties = {"elections": {
            "electoral_field": "Elecciones autonómicas",
            "place": "Comunidad de Madrid",
            "year": "2021",
            "political_parties": []
        }}

        for party in parties:
            candidates_url = self.URL_BASE_MADRID_ELECTIONS + party[0]
            party_name = NameUtils.get_party_name_from_title(party[1])
            party_abbrev = NameUtils.get_party_abbrev_from_title(party[1])

            json_party = {
                "candidates_url": candidates_url,
                "party_name": party_name,
                "party_abbrev": party_abbrev
            }
            json_parties["elections"]["political_parties"].append(json_party)

        return json_parties
