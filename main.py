from functions.functions import get_scraping_values_format_tuple
from sheets.report import check_exists_excel_file, update_sheet_row
from scrap.bloomberg_scrap import Bloomberg
from scrap.dollar_scrap import Dollar
from scrap.cme_scrap import Cme


if __name__ == '__main__':
    check_exists_excel_file()
    dollar, cme, bloomberg = Dollar(), Cme(), Bloomberg()

    # Obtengo los valores de los Scrapings
    dollar_scrap = dollar.get_data_from_pages()
    cme_scrap = cme.get_data_from_pages()
    bloomberg_scrap = bloomberg.get_data_from_pages()

    # Apendeo los Scrapings en una tupla
    scraping_tuple = get_scraping_values_format_tuple(dollar_json=dollar_scrap,
                                                      cme_json=cme_scrap,
                                                      bloomberg_json=bloomberg_scrap)

    # Actualizo la fila del excel
    update_sheet_row(scraping_tuple)
