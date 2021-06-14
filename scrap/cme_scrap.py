from functions.functions import clean_scraping_values
from scrap.interface_scraping import Scraping
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup
from log.logger import Log
import json


class Cme(Scraping):
    def __init__(self) -> None:
        super().__init__(Log())
        self.logger = Log().getLogger(__name__)

    def get_response_by_url(self, url: str) -> dict:
        try:
            request = Request(url, headers={'User-Agent': 'XYZ/3.0'})
            webpage = urlopen(request, timeout=25).read()
            html_content = soup(webpage, 'html.parser')
            response = json.loads(html_content.text)
            return response

        except Exception as e:
            print(f'Error en el retorno del response de url: "{url}", error: "{e}"')
            self.logger.error(f'Error en el retorno del response de url: "{url}", error: "{e}"')

    def get_data_from_pages(self) -> dict:
        try:
            cme_scrap = dict()

            for name_page, url in self.cme_pages.items():

                response = self.get_response_by_url(url=url)

                cme_value_list = []

                for i in range(6):
                    if (i == 0) and (response['quotes'][i]['last'] != '-'):
                        cme_value = response['quotes'][i]['last']
                        cme_last_value = clean_scraping_values('cme', cme_value)

                        cme_value_list.append(cme_last_value)

                    else:
                        cme_value = response['quotes'][i]['priorSettle']
                        cme_priorSettle_value = clean_scraping_values('cme', cme_value)

                        cme_value_list.append(cme_priorSettle_value)

                cme_scrap[name_page] = cme_value_list

            print(f'Se extrajeron correctamente los valores "[CME]" --> {cme_scrap}')
            self.logger.info(f'Se extrajeron correctamente los valores "[CME]" --> {cme_scrap}')

            return cme_scrap

        except Exception as e:
            print(f'Error en la extraccion de valores del scraping: "{e}"')
            self.logger.error(f'Error en la extraccion de valores del scraping: "{e}"')
