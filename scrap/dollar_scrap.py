from functions.functions import clean_scraping_values
from .interface_scraping import Scraping
from bs4 import BeautifulSoup
from log.logger import Log
from typing import Union
import requests
import urllib3

urllib3.disable_warnings()


class Dollar(Scraping):
    def __init__(self) -> None:
        super().__init__()
        self.logger = Log().get_logger(__name__)

    def get_response_by_url(self, url: str) -> BeautifulSoup:
        try:
            resquest = requests.get(url, verify=False, timeout=15)
            response = BeautifulSoup(resquest.content, "html.parser")
            return response

        except Exception as e:
            self.logger.error(
                f'Error in the return of the url response: "{url}", error: "{e}"'
            )

    def get_data_from_pages(self) -> dict:
        try:
            rofex_value_list = []
            dollar_scrap: dict[str, Union[str, list[str]]] = dict()

            for name_page, url in self.dollar_pages.items():

                response = self.get_response_by_url(url=url)

                if name_page == "banco_nacion":
                    dollar_value = (
                        response.find("div", id="divisas")
                        .find("tbody")
                        .find_all("td")[2]
                        .text
                    )

                    banco_nacion_value = clean_scraping_values("dollar", dollar_value)
                    dollar_scrap[name_page] = banco_nacion_value

                elif name_page == "rofex":
                    result = (
                        response.find("div", {"class": "table-responsive"})
                        .find("tbody")
                        .find_all("tr")
                    )

                    for rof in result:
                        rofex_value = clean_scraping_values("rofex", rof)
                        rofex_value_list.append(rofex_value)

                    rofex_value_list = rofex_value_list[0:5]
                    dollar_scrap[name_page] = rofex_value_list

            print(
                f'= Values "[DOLLAR]" were successfully extracted --> {dollar_scrap}\n'
            )
            self.logger.info(
                f'= Values "[DOLLAR]" were successfully extracted --> {dollar_scrap}'
            )

            return dollar_scrap

        except Exception as e:
            print(f'Error in the extraction of scraping values: "{e}"')
            self.logger.error(f'Error in the extraction of scraping values: "{e}"')
