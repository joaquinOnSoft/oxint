import logging
import urllib
import socket


class URLUtils:

    @staticmethod
    def get_html_from_url(url: str, timeout: int = -1) -> str:
        html = ""

        if url is not None and url != "":
            hdr = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) '
                              'Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'utf-8,ISO-8859-1;q=0.7,*;q=0.3',
                'Accept-Encoding': 'utf-8, iso-8859-1;q=0.5',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'}
            req = urllib.request.Request(url, headers=hdr)
            try:
                # if timeout is -1 (No limit) set a one hour limit
                if timeout == -1:
                    timeout = 3600

                with urllib.request.urlopen(req, timeout=timeout) as f:
                    charset = "utf-8"
                    if f.headers.get_content_charset() is not None:
                        charset = f.headers.get_content_charset()
                    html += f.read().decode(charset, errors='ignore')
            except socket.timeout as e:
                logging.warning(f"Timeout reading URL: {url}")
            except urllib.error.URLError as e:
                logging.warning(f"Error reading URL: {url} : {e.reason}")
            except UnicodeDecodeError as e:
                logging.warning(f"Error reading URL: {url} Unicode decode error: {e.reason}")

        return html
