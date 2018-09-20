import pandas as pd
import numpy as np
from datetime import datetime
import time
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction import text
import re
import pickle
import nltk

# Some default english stop words
stop_words = text.ENGLISH_STOP_WORDS

def remove_punctuations(word):
    return re.sub("[^a-zA-Z]", "", word)
print(remove_punctuations("it's large"))

def save_object(object, filename):
    with open(filename+'.pickle', 'wb') as outfile:
        pickle.dump(object, outfile)
        outfile.close()
def timestamp():
    return time.strftime("%b %d %Y %H:%M:%S")

def read_data(file_path):
    with open('yelp_academic_dataset_review.json', 'rb') as f:
        data = f.readlines()
    print "data read: " + timestamp()
    # remove the trailing "\n" from each line
    data = map(lambda x: x.rstrip(), data[:1000])
    print "data loaded: " + timestamp()
    data_json_str = "[" + ','.join(data) + "]"
    return pd.read_json(data_json_str)

data = read_data("yelp_academic_dataset_review.json")
print("pandas object loaded: "+timestamp())
save_object(data,'reviews_data')
#data = data.head(n=1000)
print(data.get_value(1, 'text'))
