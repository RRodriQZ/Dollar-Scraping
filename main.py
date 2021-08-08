from functions.functions import get_scraping_values_format_tuple
from sheets.report import update_sheet_row
from scrap.bloomberg_scrap import Bloomberg
from scrap.dollar_scrap import Dollar
from scrap.cme_scrap import Cme


def main() -> None:
    # Get the values of the Scrapings
    dollar_scrap = Dollar().get_data_from_pages()
    cme_scrap = Cme().get_data_from_pages()
    bloomberg_scrap = Bloomberg().get_data_from_pages()

    # Append the Scrapings in a tuple
    scraping_tuple = get_scraping_values_format_tuple(
        dollar_json=dollar_scrap,
        cme_json=cme_scrap,
        bloomberg_json=bloomberg_scrap
    )

    # Verify that the report exists -> update the Excel row
    update_sheet_row(data=scraping_tuple)


if __name__ == "__main__":
    main()
