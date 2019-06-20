import pandas as pd
import numpy as np
from sklearn.externals import joblib
from get_loc import get_loc
from sklearn.preprocessing import StandardScaler


def data_to_df(property_type, num_bathrooms, num_bedrooms, num_floors, num_recepts, postcode, post_town, new_home):
    k_model = joblib.load("week-07\project\k_model.m")

    latitude, longitude, outcode = get_loc(postcode)
    loc_class = k_model.predict(np.array([latitude, longitude]).reshape(1,2))

    df_linear = pd.read_csv('week-07\project\line.csv')
    df_linear = df_linear.set_index('index')

    df = pd.DataFrame({'latitude':latitude, 'longitude':longitude, 'property_type':property, 'num_bathrooms':num_bathrooms, 'num_bedrooms':num_bedrooms, 'num_floors':num_floors, 'num_recepts':num_recepts, 'outcode':outcode, 'post_town':post_town, 'new_home':new_home, 'loc_class':loc_class, 'price':0})




    df_linear.drop_duplicates()
    df_linear = df_linear[df_linear.price != 0]

    #df_linear = df_linear.append(df, ignore_index=True)
    df_linear = pd.get_dummies(df_linear)

    df_linear['new_price'] = df_linear['price'].apply(to_end)
    df_linear = df_linear.drop('price', axis=1)


    print(df_linear)

    data = np.array(df_linear)
    print(data[:,:-1].shape)
    scaler = StandardScaler()
    StandardScaler(copy=True, with_mean=True, with_std=True)
    scaler.fit(data)
    data = scaler.transform(data)

    print(df_linear.columns)

    return data[-1,:]

def to_end(value):
    return value

def result(data):
    rf = joblib.load(r"week-07\project\random_forest.m")
    return rf.predict(data)

if __name__ == '__main__':
    data = data_to_df('Flat', 1, 2, 0, 1, 'BS231NG', 'Weston-super-Mare', 0)
    data = data[:-1]
    length = len(data)
    print(np.exp(result(data.reshape(1, length))))