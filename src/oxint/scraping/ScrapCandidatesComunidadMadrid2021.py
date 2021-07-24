import logging
import re

from oxint.scraping.URLReader import URLReader
from oxint.utils.NameUtils import NameUtils


class ScrapCandidatesComunidadMadrid2021(URLReader):
    """
    Recover the list of candidates of a political party that has participated
    in the "Comunidad de Madrid" elections in 2021.
    https://elecciones.comunidad.madrid/es/formaciones-politicas/listado-candidaturas-proclamadas
    """

    def read(self):
        """
        Recover the list of candidates of a political party
        :return: JSON object that includes the first name, last name, election,
        year and political party abbreviation for each candidate
        """
        html = super().read()

        parties = re.findall(r"<h2 class=\"tit-partido\">(.*)</h2>", html)
        party_name = NameUtils.get_party_name_from_title(parties[0])
        party_abbrev = NameUtils.get_party_abbrev_from_title(parties[0])
        logging.debug(f"{party_name} -- {party_abbrev}")

        # Process candidates list
        candidates = re.findall(r"<li>(.*)<\/li>", html)

        json_candidates = ScrapCandidatesComunidadMadrid2021.__candidates_to_json(candidates, party_abbrev)

        return json_candidates

    @staticmethod
    def __candidates_to_json(candidates, party_abbrev: str):
        json_candidates = {"candidates": []}

        for candidate in candidates:
            underscore_index = candidate.find("-")
            if underscore_index > 0:
                underscore_index += 1
                candidate = candidate[underscore_index: len(candidate)].strip()

                logging.debug(candidate)

                first_name = NameUtils.get_first_name_from_full_name(candidate)
                last_name = NameUtils.get_last_name_from_full_name(candidate)

                json_candidate = {
                    "first_name": first_name,
                    "last_name": last_name,
                    "party_abbrev": party_abbrev,
                    "elections": "Comunidad de Madrid",
                    "year": "2021"
                }
                json_candidates["candidates"].append(json_candidate)

        return json_candidates
