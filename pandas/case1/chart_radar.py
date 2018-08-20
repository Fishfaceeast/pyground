import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

center_file = '../../../../temp/center.xls'

def result_pic(result):
    """
    雷达图的绘制
    :param result: 分类数据
    :return: 雷达图
    """
    # 解析出类别标签和种类
    labels = result.columns
    kinds = list(result.iloc[:, 0])

    # 由于在雷达图中，要保证数据闭合，这里就再添加L列，并转换为 np.ndarray
    result = pd.concat([result, result[['ZL']]], axis=1)
    centers = np.array(result.iloc[:, 1:])

    # 分割圆周长，并让其闭合
    n = len(labels)
    angle = np.linspace(0, 2 * np.pi, n, endpoint=False)
    # angle = np.concatenate((angle, [angle[0]]))

    # 绘图
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)    # 参数polar, 以极坐标的形式绘制图形

    # 画线
    for i in range(len(kinds)):
        ax.plot(angle, centers[i], linewidth=2, label=kinds[i])
        # ax.fill(angle, centers[i])  # 填充底色

    # 添加属性标签
    ax.set_thetagrids(angle * 180 / np.pi, labels)
    plt.title('different kind')
    plt.legend(loc='lower right')
    plt.show()


if __name__ == '__main__':
    result = pd.read_excel(center_file)
    result_pic(result)