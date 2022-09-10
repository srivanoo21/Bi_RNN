import logging
#from src.utils import save_json
import time
from src import logging
from src.constants import *
from src.components import DataIngestionPreparation


STAGE = "Data Ingestion and prep stage" ## <<< change stage name 



def main():
    obj = DataIngestionPreparation()


if __name__ == '__main__':
    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main()
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e