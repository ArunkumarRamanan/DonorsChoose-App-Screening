import pandas as pd
import numpy as np

import os

os.chdir('/Users/quannguyen/Downloads/kaggle-data/app-screening/code/')

train_df = pd.read_csv('../input/train.csv')

print('Shape:', train_df.shape)
print('First 5 rows:\n', train_df.head())

print('Column info:')
for column in train_df.columns:
    print(column)
    print(train_df[column].value_counts())
    print('-' * 10)
