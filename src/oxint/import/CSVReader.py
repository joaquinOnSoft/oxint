import csv
import logging


class CSVReader:
    """
    Reading CSV Files With 'csv' module.
    SEE: https://realpython.com/python-csv/#reading-csv-files-into-a-dictionary-with-csv
    """
    def __init__(self):
        self._custom_headers = None

    @property
    def custom_headers(self):
        return self._custom_headers

    @custom_headers.setter
    def custom_headers(self, custom_headers):
        self._custom_headers = custom_headers

    @custom_headers.deleter
    def custom_headers(self):
        del self._custom_headers

    def ingest(self, file_path: str, encoding: str = 'utf-8', delimiter: str = ','):
        content = {"items": []}
        with open(file_path, encoding=encoding) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=delimiter)
            line_count = 0
            num_headers = 0
            headers = None

            for row in csv_reader:
                if line_count == 0:
                    logging.debug(f'Column names are {", ".join(row)}')
                    num_headers = len(row)
                    headers = row
                    line_count += 1
                else:
                    item = {}
                    index = 0
                    for cell in row:
                        if index < num_headers:
                            if self._custom_headers is None:
                                item[headers[index]] = cell
                            else:
                                item[self._custom_headers[index]] = cell
                        index += 1

                    line_count += 1
                    content["items"].append(item)

            logging.debug(f'Processed {line_count} lines.')

        return content
