# coding:utf-8
# 2019-1-16
# softmax

import numpy as np
import random as rd

def train(feature, label, k, max_iteration, alpha):
    """
    梯度下降法
    """
    m, n = np.shape(feature)
    weights = np.mat(np.ones((n, k))) # n x k
    i = 0
    end, pre, gap = 0.0001, 1e5, 1
    while i <= max_iteration and gap > end:
        y = np.exp(feature * weights) # m x k
        if i % 500 == 0:
            error_rate = cost(y, label)
            gap = abs(error_rate - pre)
            pre = error_rate
            print("iteration: %d, error rate: %.10f, gap: %.10f" % (i, error_rate, gap))
        row_sum = -y.sum(axis=1) # 按行相加 m x 1         
        row_sum = row_sum.repeat(k, axis=1) # 每个样本都需要除以总值， 所以转换为 m x k
        y = y / row_sum # 得到-P(y|x,w)
        for x in range(m):
            y[x, label[x, 0]]  += 1

        weights = weights + (alpha / m) * feature.T * y
        i += 1
    return weights


def cost(err, label_data):
    '''
    计算损失函数值
    input:  err(mat):exp的值
            label_data(mat):标签的值
    output: sum_cost / m(float):损失函数的值
    '''
    m = np.shape(err)[0]
    sum_cost = 0.0
    for i in range(m):
        if err[i, label_data[i, 0]] / np.sum(err[i, :]) > 0:
            sum_cost -= np.log(err[i, label_data[i, 0]] / np.sum(err[i, :]))
        else:
            sum_cost -= 0
    return sum_cost / m


def load_data(num, m):
    '''
    导入测试数据
    input:  num(int)生成的测试样本的个数
            m(int)样本的维数
    output: testDataSet(mat)生成测试样本
    '''
    testDataSet = np.mat(np.ones((num, m)))
    for i in range(num):
        testDataSet[i, 1] = rd.random() * 6 - 3#随机生成[-3,3]之间的随机数
        testDataSet[i, 2] = rd.random() * 15#随机生成[0,15]之间是的随机数
    return testDataSet


def predict(test_data, weights):
    '''
    利用训练好的Softmax模型对测试数据进行预测
    input:  test_data(mat)测试数据的特征
            weights(mat)模型的权重
    output: h.argmax(axis=1)所属的类别
    '''
    h = test_data * weights
    print(h)
    return h.argmax(axis=1) # 获得最大索引位置即标签


def saveModel(file_name, weights):
    '''
    保存最终的模型
    input:  file_name(string):保存的文件名
            weights(mat):softmax模型
    '''
    f_w = open(file_name, "w")
    m, n = np.shape(weights)
    for i in range(m):
        w_tmp = []
        for j in range(n):
            w_tmp.append(str(weights[i, j]))
        f_w.write("\t".join(w_tmp) + "\n")
    f_w.close()