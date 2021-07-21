import json
import logging
import re

from oxint.scraping.URLReader import URLReader
from oxint.utils.NameUtils import NameUtils


class ScrapCandidatesMadrid2021(URLReader):

    def read(self):
        html = super().read()

        parties = re.findall(r"<h2 class=\"tit-partido\">(.*)</h2>", html)
        party_name = ScrapCandidatesMadrid2021.__get_party_name_from_title(parties[0])
        party_abbrev = ScrapCandidatesMadrid2021.__get_party_abbrev_from_title(parties[0])
        logging.debug(f"{party_name} -- {party_abbrev}")

        # Process candidates list
        candidates = re.findall(r"<li>(.*)<\/li>", html)

        json_candidates = ScrapCandidatesMadrid2021.__candidates_to_json(candidates, party_abbrev)

        print(json_candidates)

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
                    "party_abbrev": party_abbrev
                }
                json_candidates["candidates"].append(json_candidate)

        return json.dumps(json_candidates)

    @staticmethod
    def __get_party_name_from_title(title: str) -> str:
        name = None

        if title is not None:
            index_parenthesis = title.find("(")
            if index_parenthesis > 0:
                name = title[0: index_parenthesis]

        return name

    @staticmethod
    def __get_party_abbrev_from_title(title: str) -> str:
        name = None

        if title is not None:
            index_parenthesis = title.find("(") + 1
            if index_parenthesis > 0:
                name = title[index_parenthesis:].replace(")", "")

        return name

