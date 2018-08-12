import pandas as pd
catering_sale = './data/catering_sale.xls'   #餐饮数据
data = pd.read_excel(catering_sale, index_col = u'日期')
print(data.describe())