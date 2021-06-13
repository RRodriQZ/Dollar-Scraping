from log.logger import Log
import datetime


def get_str_time_now():
    """ Retorno la fecha actual en formato de String. """
    return str(datetime.datetime.now())


def clean_scraping_values(scrap, value):
    """
    Retorno el valor limpio del sraping individual en formato String.

    :param scrap: String
    :param value: String
    :return: String
    """
    logger = Log().getLogger(__name__)
    try:
        if scrap == 'dollar':
            clear_val = round(float(value), 2)
            value = str(clear_val).replace(',', '.')
            return value

        elif scrap == 'rofex':
            value = value.text.strip().split('\n')[1]
            return value

        elif scrap == 'cme':
            clear_val = round(float(value), 3)
            value = str(clear_val)
            return value

        elif scrap == 'bloomberg':
            clear_val = round(float(value), 2)
            value = str(clear_val)
            return value

    except Exception as e:
        print(f'Ocurrio un error en la limpieza del valor: "{e}"')
        logger.error(f'Ocurrio un error en la limpieza del valor: "{e}"')


def get_scraping_values_format_tuple(dollar_json, cme_json, bloomberg_json):
    """
    Retorno los 3 scrapings appendeados en formato de: [tuple]
    con el momento que se disparo el scraping.

    :param dollar_json: {dollar}
    :param cme_json: {cme}
    :param bloomberg_json: {bloomberg}
    :return: [(String)]
    """
    logger = Log().getLogger(__name__)
    try:
        time_now = get_str_time_now()

        row_list = [time_now]
        row_list.extend([dollar_json['banco_nacion']])
        row_list.extend(dollar_json['rofex'])

        row_list.extend(bloomberg_json['bloomberg_1'])
        row_list.extend(bloomberg_json['bloomberg_2'])

        row_list.extend(cme_json['cme_cotizaciones_dated_brent'])
        row_list.extend(cme_json['cme_cotizaciones_ice_brent'])
        row_list.extend(cme_json['cme_cotizaciones_wti'])
        row_list.extend(cme_json['cme_cotizaciones_cme_rbob87'])
        row_list.extend(cme_json['cme_cotizaciones_ho'])
        row_list.extend(cme_json['cme_cotizaciones_jet54_usgc'])
        row_list.extend(cme_json['cme_cotizaciones_fo_ny'])
        row_list.extend(cme_json['cme_cotizaciones_propane_opis'])
        row_list.extend(cme_json['cme_cotizaciones_butane_opis'])
        row_list.extend(cme_json['cme_cotizaciones_naphtha_cif_nwe'])

        scraping_tuple = [tuple(row_list)]

        return scraping_tuple

    except Exception as e:
        print(f'Error en la transformacion de datos, error: "{e}"')
        logger.error(f'Error en la transformacion de datos, error: "{e}"')
