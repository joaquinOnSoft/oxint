import csv
import logging


class CSVReader:
    """
    Reading CSV Files With 'csv' module.
    SEE: https://realpython.com/python-csv/#reading-csv-files-into-a-dictionary-with-csv
    """
    def __init__(self):
        self._headers = None

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def md(self, headers):
        self._headers = headers

    def ingest(self, file_path: str, encoding: str = 'utf-8', delimiter: str = ','):
        content = {"items": []}
        with open(file_path, encoding=encoding) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=delimiter)
            line_count = 0
            num_headers = 0

            for row in csv_reader:
                if line_count == 0:
                    logging.debug(f'Column names are {", ".join(row)}')
                    num_headers = len(row)
                    if self._headers is None:
                        self._headers = row
                    line_count += 1
                else:
                    item = {}
                    index = 0
                    for cell in row:
                        if index < num_headers:
                            item[self.headers[index]] = cell
                        index += 1

                    line_count += 1
                    content["items"].append(item)

            logging.debug(f'Processed {line_count} lines.')

        return content
