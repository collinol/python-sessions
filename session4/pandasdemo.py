"""References
https://www.transitchicago.com/data/
https://pandas.pydata.org/pandas-docs/stable/reference/index.html#api
https://www.w3schools.com/python/pandas/default.asp
https://re-thought.com/how-to-change-or-update-a-cell-value-in-python-pandas-dataframe/
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def process_pandas(csv_file: str, output: str) -> None:
    """ main function that calculates average from input csv file and write to output, using pandas"""
    # open csv file and do something with contents
    df = pd.read_csv(csv_file)
    average = df['rides'].sum() / len(df)
    import pdb
    pdb.set_trace()
    # df.head()
    # df.info()

def numpy():
    arr1 = np.array([[6, 2, 4],
                     [5, 7, 3]])

    arr2 = np.sort(arr1, axis=0)

    arr3 = np.sort(arr1, axis=1)

    arr4 = np.sort(arr1, axis=-1)

    print('arr1 sorted along rows\n', arr2)
    print('arr1 sorted along columnc\n', arr3)
    print('arr1 sorted along last axis which in this case is column\n', arr4)


    dt = [('color', 'S10'), ('size', int), ('price', float)]
    values = [('red', 28, 599.99), ('teal', 34, 999.99), ('lavender', 34, 799.99)]
    arr1 = np.array(values, dtype=dt)

    arr2 = np.sort(arr1, order=['size', 'price'])
    print('Original array\n', arr1)
    print('arr1 sorted by size and than price\n', arr2)
    arr = np.identity(3)  # numpy method to create an identity matrix of size 3x3

    rank = np.linalg.matrix_rank(arr)

    inv = np.linalg.inv(arr)

    print('Identity Matrix:\n', arr)
    print('Rank of matrix:\n', rank)
    print('inverse of matrix:\n', inv)
    import pdb
    pdb.set_trace()

if __name__ == '__main__':
    #process_pandas('cta_data.csv', 'output.csv')
    numpy()
