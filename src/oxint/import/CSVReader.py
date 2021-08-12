import csv
import logging
from os import path


class CSVReader:

    @staticmethod
    def ingest(file_path: str, encoding: str = 'utf-8', delimiter: str = ','):
        content = {"items": []}
        with open(file_path, encoding=encoding) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=delimiter)
            line_count = 0
            headers = None
            num_headers = 0

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
                            item[headers[index]] = cell
                        index += 1

                    line_count += 1
                    content["items"].append(item)

            logging.debug(f'Processed {line_count} lines.')

        return content
