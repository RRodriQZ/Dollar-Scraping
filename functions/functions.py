from datetime import datetime
from log.logger import Log


# GLOBAL VALUES #
logger = Log().get_logger(__name__)


def get_str_time_now() -> str:
    """Retorno la fecha actual en formato de String"""
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def clean_scraping_values(scrap: str, value: str) -> str:
    """Retorno el valor limpio del sraping individual en formato String

    :param scrap: str
    :param value: str
    :return: str
    """
    try:
        if scrap == "dollar":
            rounded_value = round(float(value), 2)
            value = str(rounded_value).replace(",", ".")
            return value

        elif scrap == "rofex":
            value = value.text.strip().split("\n")[1]
            return value

        elif scrap == "cme":
            rounded_value = round(float(value), 3)
            value = str(rounded_value)
            return value

        elif scrap == "bloomberg":
            rounded_value = round(float(value), 2)
            value = str(rounded_value)
            return value

    except Exception as e:
        print(f'Ocurrio un error en la limpieza del valor: "{e}"')
        logger.error(f'Ocurrio un error en la limpieza del valor: "{e}"')


def get_scraping_values_format_tuple(dollar_json: dict, cme_json: dict, bloomberg_json: dict) -> tuple:
    """Retorno los 3 scrapings appendeados en formato de: Tuple con el momento que se disparo el scraping

    :param dollar_json: dict[str, Union[str, list[str]]]
    :param cme_json: dict[str, list[str]]
    :param bloomberg_json: dict[str, list[str]]
    :return: tuple
    """
    try:
        time_now = get_str_time_now()

        row_list = [time_now]
        row_list.extend([dollar_json["banco_nacion"]])
        row_list.extend(dollar_json["rofex"])

        row_list.extend(bloomberg_json["bloomberg_1"])
        row_list.extend(bloomberg_json["bloomberg_2"])

        row_list.extend(cme_json["cme_cotizaciones_dated_brent"])
        row_list.extend(cme_json["cme_cotizaciones_ice_brent"])
        row_list.extend(cme_json["cme_cotizaciones_wti"])
        row_list.extend(cme_json["cme_cotizaciones_cme_rbob87"])
        row_list.extend(cme_json["cme_cotizaciones_ho"])
        row_list.extend(cme_json["cme_cotizaciones_jet54_usgc"])
        row_list.extend(cme_json["cme_cotizaciones_fo_ny"])
        row_list.extend(cme_json["cme_cotizaciones_propane_opis"])
        row_list.extend(cme_json["cme_cotizaciones_butane_opis"])
        row_list.extend(cme_json["cme_cotizaciones_naphtha_cif_nwe"])

        scraping_tuple = tuple(row_list)

        return scraping_tuple

    except Exception as e:
        print(f'Error en la transformacion de datos, error: "{e}"')
        logger.error(f'Error en la transformacion de datos, error: "{e}"')
