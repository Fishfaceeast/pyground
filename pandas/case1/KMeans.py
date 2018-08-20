import pandas as pd
from sklearn.cluster import KMeans
from math import pi

# read data
data_file = '../../../../temp/zscored_data.xls'
result_file = '../../../../temp/kmeans.xls'
center_file = '../../../../temp/center.xls'

k = 5  #聚类的类别
iteration = 500  #聚类最大循环次数

data = pd.read_excel(data_file)

model = KMeans(n_clusters=k, n_jobs=4, max_iter=iteration)
model.fit(data)  #训练模型

r1 = pd.Series(model.labels_).value_counts()
r2 = pd.DataFrame(model.cluster_centers_)
r = pd.concat([r1, r2], axis=1)

r.columns = [u'类别数目'] + list(data.columns)  #重命名表头
r2.columns = list(data.columns)
r2.to_excel(center_file)

r = pd.concat([data, pd.Series(model.labels_, index=data.index)], axis=1)  #详细输出每个样本对应的类别 知道每个客户属于哪个大类这也是最基本的目的
r.columns = list(data.columns) + [u'聚类类别']  #重命名表头
r.to_excel(result_file)  #保存结果


