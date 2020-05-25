# coding:UTF-8
# 2018-10-17
# DBSCAN(Density-Based Spatial Clustering of Aplication with Noise)

"""
在基于密度的聚类算法中，通过在数据集中寻找被低密度分离的高密度区域，将分离出来的低密度区域作为一个独立的类别。

将数据点分为三种类型: 核心，边界， 噪点

DBSCAN中的三种概念:
    a. 直接密度可达(directly density-reachable)
    b. 密度可达(density-reachable)
    c. 密度连接(density-connected)
"""

import numpy as np 
import math

MinPts = 5 # 最小区域样本数


def loadData(file_path):
    '''
    导入数据
    '''
    f = open(file_path)
    data = []
    for line in f.readlines():
        data_tmp = []
        lines = line.strip().split("\t")
        for x in lines:
            data_tmp.append(float(x.strip()))
        data.append(data_tmp)
    f.close()
    return np.mat(data)


def epsilon(data, MinPts):
    """
    计算邻域半径
    """
    m, n = np.shape(data)
    x_max = np.max(data, 0)
    x_min = np.min(data, 0)

    eps = ((np.prod(x_max - x_min) * MinPts * math.gamma(0.5 * n + 1)) / (m * math.sqrt(math.pi ** n))) ** (1.0 / n)

    return eps 


def distance(data):
    """
    计算数据中每个点之间的欧拉距离
    """
    m, n = np.shape(data)
    dist = np.mat(np.zeros((m, m)))

    for i in range(m):
        for j in range(i, m):
            tmp_sum = 0
            for k in range(n):
                tmp_sum += (data[i, k] - data[j, k]) * (data[i, k] - data[j, k])
            dist[i, j] = np.sqrt(tmp_sum)
            dist[j, i] = dist[i, j] # 两个点之间距离是相同的

    return dist


def findEps(distance, eps):
    """
    寻找领域内点的索引
    """
    index = []
    n = np.shape(distance)[1]
    for j in range(n):
        if distance[0, j] <= eps:
            index.append(j)

    return index


def dbscan(data, eps, MinPts):
    """
    基于密度的聚类
    a. 对每一个点i进行处理
    b. 找到点i到其它点的距离
    c. 寻找领域内的点
    d. 判断领域内点的数目并进行处理
        1. 边界
        2. 噪点
        3. 核心点
            判断是否密度可达
    """
    m = np.shape(data)[0]

    # 标记点的类型, 核心点为1, 边界为0, 噪音点为-1
    types = np.mat(np.zeros((1, m)))
    sub_class = np.mat(np.zeros((1, m)))

    # 标记点是否已经处理过, 0:未处理
    dealed = np.mat(np.zeros((m, 1)))

    # 计算每个样本之间的欧拉距离
    dist = distance(data)

    # 用于标记簇类
    number = 1

    # 对每一个点进行处理
    for i in range(m):
        if dealed[i, 0] == 0:
            D = dist[i, :] # 第i个样本与其他点的距离
            ind = findEps(D, eps)   # 找到与当前点距离小于eps的点的索引

            # 边界点
            if len(ind) > 1 and len(ind) < MinPts + 1:
                types[0, i] = 0 # 将当前点标记为边界点
                sub_class[0, i] = 0 # 将当前点归于第0个簇类

            # 噪音点
            if len(ind) == 1:
                types[0, i] = -1
                sub_class[0, i] = -1
                dealed[i, 0] = 1

            # 核心点
            if len(ind) >= MinPts + 1:
                types[0, i] = 1
                for x in ind:
                    sub_class[0, x] = number    # 将点标记为number值，表示属于第Number个簇类

                # 判断核心点是否密度可达
                while len(ind) > 0:
                    dealed[ind[0], 0] = 1   # 标记ind[0]点为已处理，当前点表示为K
                    D = dist[ind[0], :]     # k点与其它所有点之间的欧拉距离
                    tmp = ind[0]            # 记k点为tmp
                    del ind[0]              # 删除K点在ind中的记录
                    index = findEps(D, eps) # 找到与当前点距离小于eps的点的索引

                    # 处理非噪音点
                    if len(index) > 1:  # 如果周围存在属于一个簇的点
                        for x in index: # 将周围的点标记为number值的簇
                            sub_class[0, x] = number

                        # 判断点类型
                        if len(index) >= MinPts + 1:    # 如果当前处理点所在簇类的个数大于最小簇类数
                            types[0, tmp] = 1           # 则标记为核心点
                        else:
                            types[0, tmp] = 0           # 否则标记为非核心点


                        for j in range(len(index)):     
                            if dealed[index[j], 0] == 0:    
                                dealed[index[j], 0] = 1         # 如果与K点同一个簇类的点没有被处理过则标记为处理过
                                ind.append(index[j])            # 将k点同一个簇类的点放入ind中，在下一个循环中处理
                                # sub_class[0, index[j]] = number # 这一步可以不需要，与145行代码重复了
                number += 1 # 簇类标记数+1

    # 最后处理未分类的点为噪点
    inds = ((sub_class == 0).nonzero())[1]
    for x in inds:
        sub_class[0, x] = -1
        types[0, x] = -1

    return types, sub_class


if __name__ == "__main__":
    # 1、导入数据
    print("loading data...")
    data = loadData("data.txt")

    print("training...")
    # 2、计算半径
    eps = epsilon(data, MinPts)
    # 3、利用DBSCAN算法进行训练
    types, sub_class = dbscan(data, eps, MinPts)
    print("finish!\n")

    
    print(types)
    print(sub_class)