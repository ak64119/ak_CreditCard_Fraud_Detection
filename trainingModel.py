"""
This is the Entry point for Training the Machine Learning Model.

Written By: Akshay Kochhar
Version: 1.0
Revisions: None

"""

# Doing the necessary imports
from sklearn.model_selection import train_test_split
from data_ingestion import data_loader
from data_preprocessing import preprocessing
from data_preprocessing import clustering
from best_model_finder import tuner
from file_operations import file_methods
from application_logging import logger