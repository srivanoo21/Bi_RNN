import tensorflow_datasets as tfds
from src.constants import *
import tensorflow as tf
from src import logging


class DataIngestionPreparation:
    def __init__(self,):
        self.dataset_name = "imdb_reviews"

    def load_data(self):
        dataset, info = tfds.load(name=dataset_name, with_info=True, as_supervised=True)
        self.train_ds = self.test_ds = dataset["train_ds"], dataset["test_ds"]
        logging.info(f"{self.dataset_name} dataset downloaded with info:\n{info}")

    def shuffle_and_batch(self):
        pass

    def encode_on_train_data():
        pass

    def save_encoder(self):
        pass 

    def save_train_and_test_data(self):
        pass