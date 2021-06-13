from openpyxl import Workbook, load_workbook
from configparser import ConfigParser
from log.logger import Log
import os


# GLOBAL VALUES #
config = ConfigParser()
config.read('config.ini')
REPORT_FILE = config['File']['excel_file']
HEAD_COLUMN = config['File']['head']


def check_exists_excel_file():
    logger = Log().getLogger(__name__)
    try:
        print(f'========================= INICIANDO EL SCRIPT =========================')
        if os.path.exists(REPORT_FILE):
            print(f'=========== Actualizando... el archivo "{REPORT_FILE}" ===========')
            logger.info(f'========================= INICIANDO EL SCRAPING =========================')
            logger.info(f'=========== Actualizando... el archivo "{REPORT_FILE}" ===========')

        else:
            print(f'=========== No existe el archivo: "{REPORT_FILE}" ===========')

            wb = Workbook()
            wb.save(REPORT_FILE)
            sheet = wb.active

            head_column = HEAD_COLUMN.split(',')
            head_titles = [tuple(head_column)]

            for title in head_titles:
                sheet.append(title)

            wb.save(REPORT_FILE)

            print(f'Generado un nuevo archivo: "{REPORT_FILE}"')
            logger.info(f'=========== No existe el archivo: "{REPORT_FILE}" ===========')
            logger.info(f'Generado un nuevo archivo: "{REPORT_FILE}"')

    except Exception as e:
        print(f'ERROR en la Generacion del excel "{REPORT_FILE}", error: "{e}"')
        logger.error(f'ERROR en la Generacion del excel "{REPORT_FILE}", error: "{e}"')


def update_sheet_row(row):
    logger = Log().getLogger(__name__)
    try:
        wb = load_workbook(REPORT_FILE)
        sheet = wb.active

        for r in row:
            sheet.append(r)

        wb.save(REPORT_FILE)

        print(f'=========== Se actualizo correctamente el reporte con la nueva informacion ===========')
        logger.info(f'=========== Se actualizo correctamente el reporte con la nueva informacion ===========')

    except Exception as e:
        print(f'ERROR en la actualizacion del excel, error: "{e}"')
        logger.error(f'ERROR en la actualizacion del excel, error: "{e}"')
