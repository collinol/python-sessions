from pandas import read_csv as reader
from pandas import DataFrame as Dataframe
import matplotlib.pyplot as plt
import numpy as np

"""
https://www.transitchicago.com/data/
https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
https://pandas.pydata.org/pandas-docs/stable/reference/index.html#api
"""
def pandas_demo():
    dataframe = Dataframe(
        {
            "name": ["Collin", "Eric", "Rohini"],
            "company": ["tempus"]*3
        }
    )
    cta_df = reader("cta_data.csv")
    """
    
    get location of multiple conditions
    
    df.loc[ (df['col a'] == x) & (df['col b'] == y) ]
    
    """

def numpy():
    arr1 = np.array(
        [
            [6, 2, 4],
            [5, 7, 3]
        ]
    )

    arr2 = np.sort(arr1, axis=1)
    print(arr1)
    print(arr2)
    xx = [1, 2, 5, 3, 9, 0].sort()
    import pdb
    pdb.set_trace()

if __name__ == '__main__':
    numpy()