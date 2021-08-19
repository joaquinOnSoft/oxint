import logging

from bs4 import BeautifulSoup

from oxint.utils.TimeUtils import TimeUtils
from oxint.utils.URLUtils import URLUtils


class ScrapInfocif:

    INFOCIF_URL_BASE = "http://www.infocif.es"

    def search_company_by_cif(self, cif: str):
        company_info = None

        if cif is not None:
            url = self.INFOCIF_URL_BASE + f"/general/empresas-informacion-listado-empresas.asp?Buscar={cif}"

            logging.debug(f"URL: {url}")
            html = URLUtils.get_html_from_url(url)
            soup = BeautifulSoup(html, "html.parser")

            # recover headers from "Company information" section
            company_info_field_names = ScrapInfocif.__get_company_information_field_names(soup)
            # recover values from "Company information" section
            company_info_field_values = ScrapInfocif.__get_company_information_field_values(soup)
            # Mix company information (field names and values)
            company_info = ScrapInfocif.__mix_field_names_with_values(company_info_field_names, company_info_field_values)
        return company_info

    @staticmethod
    def __get_company_information_field_names(soup):
        """
        Recover field names from "Información de la compañía" section
        :param soup:
        :return: Array with the field names
        """
        headers = []

        headers_col_1 = soup.find_all("strong", class_="col-md-2 col-sm-3 col-xs-12 cb fwb")
        headers_col_2 = soup.find_all("strong", class_="col-md-4 col-sm-4 col-xs-12 cb fwb")

        for header in headers_col_1:
            headers.append(ScrapInfocif.__standardize_field_names(header.contents[0]))
        for header in headers_col_2:
            headers.append(ScrapInfocif.__standardize_field_names(header.contents[0]))

        return headers

    @staticmethod
    def __standardize_field_names(field_name):
        if field_name == 'CIF':
            field = "cif"
        elif field_name == 'Antigüedad':
            field = "since"
        elif field_name == 'Domicilio':
            field = "address"
        elif field_name == 'Teléfono':
            field = "phone"
        elif field_name == 'Web':
            field = "web"
        elif field_name == 'Registro':
            field = "register"
        elif field_name == 'Sector':
            field = "sector"
        elif field_name == 'Nº de empleados':
            field = "num_employees"
        elif field_name == 'Matriz':
            field = "parent_company"
        elif field_name == 'Estado:':
            field = "state"
        elif field_name == 'Información Crediticia:':
            field = "credit information"
        else:
            field = "unknown"
            logging.warning(f"Unknown field {field_name}")

        return field

    @staticmethod
    def __get_company_information_field_values(soup):
        """
        Recover field values from "Información de la compañía" section
        :param soup:
        :return: Array with the field values
        """
        values = []

        values_cif = soup.find_all("h2", class_="editable col-md-10 col-sm-9 col-xs-12 mb10 text-right")
        values_col_1 = soup.find_all("p", class_="editable col-md-10 col-sm-9 col-xs-12 mb10 text-right")
        values_col_2 = soup.find_all("p", class_="editable col-md-8 col-sm-8 col-xs-12 mb10 text-right")

        if values_cif is not None and len(values_cif) == 1:
            values.append(ScrapInfocif.__trim(values_cif[0].contents[0]))
        values += ScrapInfocif.__manage_company_info_values(values_col_1)
        values += ScrapInfocif.__manage_company_info_values(values_col_2)

        return values

    @staticmethod
    def __manage_company_info_values(values_in_column):
        values = []
        for value in values_in_column:
            links = value.find_all("a")
            if links is not None and len(links) > 0:
                values.append(ScrapInfocif.__trim(links[0].contents[0]))
            else:
                values.append(ScrapInfocif.__trim(value.contents[0]))

        return values

    @staticmethod
    def __mix_field_names_with_values(company_info_field_names, company_info_field_values):
        """
        Mix company information (field names and values)
        :param company_info_field_names: Array with field names
        :param company_info_field_values: Array with field values
        :return: dictionary with the values assigned to the right field name
        """
        mix = {}
        if company_info_field_names is not None and \
                company_info_field_values is not None and\
                len(company_info_field_names) == len(company_info_field_values):

            for i, val in enumerate(company_info_field_names):
                mix[val] = company_info_field_values[i]

            mix["last_update"] = TimeUtils.now()

        return mix

    @staticmethod
    def __trim(string: str) -> str:
        if string is not None:
            string = string.replace("\r\n", " ").replace(u'\xa0', u' ').strip()
        return string
