import pandas as pd
import numpy as np

# read data
data_file = '../../../../temp/data_clean.xls'
result_file = '../../../../temp/zscored_data.xls'

data = pd.read_excel(data_file)

data = data.loc[:, ['FFP_DATE', 'LOAD_TIME', 'FLIGHT_COUNT', 'avg_discount', 'SEG_KM_SUM', 'LAST_TO_END']]

data['L'] = pd.to_datetime(data['LOAD_TIME']) - pd.to_datetime(data['FFP_DATE'])

data['L'] = data['L'] / np.timedelta64(1, 'D')

data = data.loc[:, ['L', 'FLIGHT_COUNT', 'avg_discount', 'SEG_KM_SUM', 'LAST_TO_END']]

data = (data - data.mean())/data.std()

data.columns = ['Z'+i for i in data.columns]

data.to_excel(result_file)
