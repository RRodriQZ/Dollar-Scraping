from functions.functions import clean_scraping_values
from .interface_scraping import Scraping
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup
from log.logger import Log
import json


class Cme(Scraping):
    def __init__(self) -> None:
        super().__init__()
        self.logger = Log().get_logger(__name__)

    def get_response_by_url(self, url: str) -> dict:
        try:
            request = Request(url, headers={"User-Agent": "XYZ/3.0"})
            webpage = urlopen(request, timeout=self.time_out).read()
            html_content = soup(webpage, "html.parser")
            response = json.loads(html_content.text)
            return response

        except Exception as e:
            self.logger.error(
                f'Error in the return of the url response: "{url}", error: "{e}"'
            )

    def get_data_from_pages(self) -> dict:
        try:
            cme_scrap: dict[str, list[str]] = dict()

            for name_page, url in self.cme_pages.items():

                response = self.get_response_by_url(url=url)

                cme_value_list = []

                for i in range(6):
                    if (i == 0) and (response["quotes"][i]["last"] != "-"):
                        cme_value = response["quotes"][i]["last"]
                        cme_last_value = clean_scraping_values("cme", cme_value)

                        cme_value_list.append(cme_last_value)

                    else:
                        cme_value = response["quotes"][i]["priorSettle"]
                        cme_priorSettle_value = clean_scraping_values("cme", cme_value)

                        cme_value_list.append(cme_priorSettle_value)

                cme_scrap[name_page] = cme_value_list

            print(f'= Values "[CME]" were successfully extracted --> {cme_scrap}\n')
            self.logger.info(
                f'= Values "[CME]" were successfully extracted --> {cme_scrap}'
            )

            return cme_scrap

        except Exception as e:
            print(f'Error in the extraction of scraping values: "{e}"')
            self.logger.error(f'Error in the extraction of scraping values: "{e}"')
