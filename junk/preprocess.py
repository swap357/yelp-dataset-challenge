'''
This file includes data cleaning and preprocessing
'''
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
import load_panda_obj

def read_data(file_path):
	return pd.read_csv(file_path)

def split_data(data):
	return train_test_split(data)

data = load_panda_obj.reviews_data_obj()

train_data, test_data = split_data(data)
del data
train_data.to_csv("train.csv", sep=",", encoding='utf-8')
test_data.to_csv("test.csv", sep=",", encoding='utf-8')