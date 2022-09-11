import logging
#from src.utils import save_json
import time
from src import logging
from src.constants import *
from src.components import DataIngestionPreparation


STAGE = "Data Ingestion and prep stage" ## <<< change stage name 



def main():
    data_ing_prep_obj = DataIngestionPreparation()
    data_ing_prep_obj.load_data()
    data_ing_prep_obj.shuffle_and_batch()
    data_ing_prep_obj.encode_on_train_data()



if __name__ == '__main__':
    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main()
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e