import pandas as pd

# read data
data_file = '../../../../data/air_data.csv'
result_file = '../../../../temp/explore.xls'

data = pd.read_csv(data_file, encoding='utf-8')
explore = data.describe(percentiles=[], include='all').T  #行列转换
explore['null'] = len(data)-explore['count']
print(explore)

explore = explore[['null', 'max', 'min']]
explore.columns = [u'空值数', u'最大值', u'最小值']

explore.to_excel(result_file)
