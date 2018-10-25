import pickle
def reviews_data_obj():
    try:
        f = open('reviews_data.pickle', 'rb')
        reviews_obj = pickle.load(f)
        f.close()
        return reviews_obj
    except:
        print "Error."
        return None