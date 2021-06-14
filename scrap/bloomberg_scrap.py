from functions.functions import clean_scraping_values
from scrap.interface_scraping import Scraping
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup
from log.logger import Log
import json


class Bloomberg(Scraping):
    def __init__(self) -> None:
        super().__init__(Log())
        self.logger = Log().getLogger(__name__)

    def get_response_by_url(self, url: str) -> dict:
        try:
            request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(request, timeout=10).read()
            html_content = soup(webpage, 'html.parser')
            response = json.loads(html_content.text)
            return response

        except Exception as e:
            print(f'Error en el retorno del response de url: "{url}", error: "{e}"')
            self.logger.error(f'Error en el retorno del response de url: "{url}", error: "{e}"')

    def get_data_from_pages(self) -> dict:
        try:
            bloomberg_scrap = dict()

            for name_page, url in self.bloomberg_pages.items():

                response = self.get_response_by_url(url=url)
                bloomberg_value_list = []

                for i in range(2):
                    bloomberg_price = response["fieldDataCollection"][i]['price']
                    bloomberg_priceChange = response["fieldDataCollection"][i]['priceChange1Day']

                    bloomberg_price_value = clean_scraping_values('bloomberg', bloomberg_price)
                    bloomberg_priceChange_value = clean_scraping_values('bloomberg', bloomberg_priceChange)

                    bloomberg_value_list.append(bloomberg_price_value)
                    bloomberg_value_list.append(bloomberg_priceChange_value)

                bloomberg_scrap[name_page] = bloomberg_value_list

            print(f'Se extrajeron correctamente los valores "[BLOOMBERG]" --> {bloomberg_scrap}')
            self.logger.info(f'Se extrajeron correctamente los valores "[BLOOMBERG]" --> {bloomberg_scrap}')

            return bloomberg_scrap

        except Exception as e:
            print(f'Error en la extraccion de valores del scraping: "{e}"')
            self.logger.error(f'Error en la extraccion de valores del scraping: "{e}"')
