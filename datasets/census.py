from pathlib import Path
import pandas as pd
from fmmd.definitions import PROJECT_ROOT,DATA_DIR

census_small_constraints = {
    2: {
        5: [[1, 3], [2, 4]],
        10: [[4, 6], [4, 6]],
        15: [[5, 9], [6, 10]],
        20: [[8, 12], [8, 12]],
        25: [[9, 15], [10, 16]],
        30: [[12, 18], [12, 18]],
        35: [[13, 21], [14, 22]],
        40: [[15, 23], [16, 26]],
        45: [[17, 27], [18, 28]],
        50: [[19, 29], [20, 32]],
    },
    7: {
        10: [[1, 3], [1, 2], [1, 3], [1, 3], [1, 2], [1, 2], [1, 2]],
        15: [[2, 4], [1, 2], [1, 3], [2, 4], [1, 3], [1, 3], [1, 3]],
        20: [[3, 5], [1, 3], [2, 4], [2, 4], [1, 3], [2, 4], [2, 4]],
        25: [[4, 6], [2, 4], [3, 5], [3, 5], [2, 4], [2, 4], [2, 4]],
        30: [[4, 6], [2, 4], [4, 6], [4, 6], [3, 5], [3, 5], [3, 5]],
        35: [[4, 8], [2, 4], [4, 6], [4, 8], [4, 6], [4, 6], [4, 6]],
        40: [[5, 9], [3, 5], [4, 8], [5, 9], [4, 6], [4, 8], [4, 6]],
        45: [[6, 10], [3, 5], [5, 9], [6, 10], [4, 8], [4, 8], [4, 8]],
        50: [[7, 11], [4, 6], [6, 10], [6, 10], [4, 8], [5, 9], [5, 9]],
    },
    14: {
        15: [
            [1, 3],
            [1, 2],
            [1, 2],
            [1, 2],
            [1, 2],
            [1, 2],
            [1, 2],
            [1, 2],
            [1, 2],
            [1, 2],
            [1, 2],
            [1, 2],
            [1, 2],
            [1, 2],
        ],
        20: [
            [1, 3],
            [1, 2],
            [1, 3],
            [1, 3],
            [1, 2],
            [1, 2],
            [1, 2],
            [1, 3],
            [1, 2],
            [1, 3],
            [1, 3],
            [1, 2],
            [1, 2],
            [1, 2],
        ],
        25: [
            [1, 3],
            [1, 2],
            [1, 3],
            [1, 3],
            [1, 3],
            [1, 3],
            [1, 2],
            [1, 3],
            [1, 2],
            [1, 3],
            [1, 3],
            [1, 3],
            [1, 3],
            [1, 3],
        ],
        30: [
            [2, 4],
            [1, 3],
            [1, 3],
            [1, 3],
            [1, 3],
            [1, 3],
            [1, 3],
            [2, 4],
            [1, 2],
            [1, 3],
            [2, 4],
            [1, 3],
            [1, 3],
            [1, 3],
        ],
        35: [
            [2, 4],
            [1, 3],
            [2, 4],
            [2, 4],
            [1, 3],
            [1, 3],
            [1, 3],
            [1, 3],
            [1, 3],
            [2, 4],
            [2, 4],
            [1, 3],
            [2, 4],
            [2, 4],
        ],
        40: [
            [2, 4],
            [1, 3],
            [2, 4],
            [2, 4],
            [2, 4],
            [2, 4],
            [1, 3],
            [3, 5],
            [1, 3],
            [2, 4],
            [2, 4],
            [2, 4],
            [2, 4],
            [2, 4],
        ],
        45: [
            [3, 5],
            [1, 3],
            [2, 4],
            [3, 5],
            [2, 4],
            [2, 4],
            [1, 3],
            [3, 5],
            [2, 4],
            [2, 4],
            [3, 5],
            [2, 4],
            [2, 4],
            [3, 5],
        ],
        50: [
            [4, 6],
            [2, 4],
            [3, 5],
            [3, 5],
            [2, 4],
            [2, 4],
            [2, 4],
            [3, 5],
            [1, 3],
            [3, 5],
            [3, 5],
            [2, 4],
            [3, 5],
            [3, 5],
        ],
    },
}

census_constraints = {
    2:{10: [[4, 6], [4, 6]], 20: [[8, 12], [8, 12]], 30: [[12, 18], [12, 18]],
          40: [[15, 23], [16, 26]], 50: [[19, 29], [20, 32]], 60: [[23, 35], [24, 38]],
          70: [[27, 41], [28, 44]], 80: [[31, 47], [32, 50]], 90: [[35, 53], [36, 56]],
          100: [[38, 58], [41, 63]]},
    7:  {10: [[1, 3], [1, 2], [1, 3], [1, 3], [1, 2], [1, 2], [1, 2]], 20: [[3, 5], [1, 3], [1, 3], [2, 4], [2, 4], [2, 4], [2, 4]],
          30: [[4, 6], [2, 4], [4, 6], [4, 6], [3, 5], [3, 5], [3, 5]], 40: [[5, 9], [4, 6], [4, 8], [5, 9], [4, 6], [4, 6], [4, 6]],
          50: [[7, 11], [4, 6], [6, 10], [6, 10], [4, 8], [5, 9], [5, 9]], 60: [[8, 14], [4, 8], [7, 11], [8, 12], [6, 10], [6, 10], [6, 10]],
          70: [[9, 15], [5, 9], [8, 14], [9, 15], [7, 11], [8, 12], [7, 11]], 80: [[12, 18], [6, 10], [9, 15], [10, 16], [8, 12], [8, 14], [8, 14]],
          90: [[12, 20], [7, 11], [11, 17], [12, 18], [9, 15], [9, 15], [9, 15]], 100: [[14, 22], [8, 12], [12, 18], [13, 21], [10, 16], [11, 17], [10, 16]]},
    14: {20: [[1, 3], [1, 2], [1, 3], [1, 3], [1, 2], [1, 2], [1, 2], [1, 3], [1, 2], [1, 3], [1, 3], [1, 2], [1, 2], [1, 2]],
          30: [[2, 4], [1, 3], [1, 3], [1, 3], [1, 3], [1, 3], [1, 3], [2, 4], [1, 2], [1, 3], [2, 4], [1, 3], [1, 3], [1, 3]],
          40: [[3, 5], [1, 3], [2, 4], [2, 4], [2, 4], [2, 4], [1, 3], [3, 5], [1, 3], [2, 4], [1, 3], [2, 4], [2, 4], [2, 4]],
          50: [[4, 6], [2, 4], [3, 5], [3, 5], [2, 4], [2, 4], [2, 4], [3, 5], [1, 3], [3, 5], [3, 5], [2, 4], [3, 5], [3, 5]],
          60: [[4, 8], [2, 4], [4, 6], [3, 5], [3, 5], [3, 5], [2, 4], [4, 6], [2, 4], [4, 6], [4, 6], [3, 5], [3, 5], [4, 6]],
          70: [[4, 8], [3, 5], [4, 6], [4, 8], [3, 5], [4, 6], [3, 5], [4, 8], [2, 4], [4, 6], [4, 8], [4, 6], [4, 6], [4, 8]],
          80: [[5, 9], [3, 5], [4, 8], [5, 9], [4, 6], [4, 6], [3, 5], [5, 9], [4, 6], [4, 8], [5, 9], [4, 6], [4, 8], [4, 8]],
          90: [[6, 10], [4, 6], [5, 9], [5, 9], [4, 8], [4, 8], [4, 6], [6, 10], [3, 5], [5, 9], [6, 10], [4, 8], [4, 8], [5, 9]],
          100: [[7, 11], [4, 6], [6, 10], [6, 10], [4, 8], [4, 8], [4, 6], [7, 11], [4, 8], [6, 10], [6, 10], [5, 9], [5, 9], [6, 10]]}
}
def load_census_small(grouping:int,data_dir:Path=DATA_DIR):
    census_df = pd.read_csv(data_dir/"census_small.csv",header=None)
    id = census_df.iloc[:,0].values.copy(order='C')
    features = census_df.iloc[:,4:].values.astype(float).copy(order='C')
    groups = census_df.iloc[:,grouping].values.copy(order='C')
    return id,features,groups

def load_census(grouping:int,data_dir:Path=DATA_DIR):
    census_df = pd.read_csv(data_dir/"census.csv",header=None)
    id = census_df.iloc[:,0].values.copy(order='C')
    features = census_df.iloc[:,4:].values.astype(float).copy(order='C')
    groups = census_df.iloc[:,grouping].values.copy(order='C')
    return id,features,groups