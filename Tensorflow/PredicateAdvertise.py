# -*- coding:utf-8 -*-
# 多层感知器预测销售情况
# 将一种广告投放到TV、newspaper、radio上时不同组合的情况会对应不同的销售量。
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import os

DATA_DIR = ''

# 数据结构和数据分析工具
data = pd.read_csv("Advertising.csv")
print(data.head())
# plt.scatter(data.TV,data.sales)
plt.show()
#  x取值除去第一列和最后一列的值取出所有投放广告的值
x = data.iloc[:, 1:-1]
#  y取值最后一列销量的值
y = data.iloc[:, -1]
# print(x)
# print(y)
# 建立顺序模型【输入层：一个多层感知器(隐含层10层Dense(10),形状input_shape=(3,)3维,激活函数activation="relu")，输出层：因为输出是一个值所以维度1】
model = tf.keras.Sequential([tf.keras.layers.Dense(10, input_shape=(3,), activation='relu'), tf.keras.layers.Dense(1)])
# 打印出模型概述信息
model.summary()
# 返回包含模型配置信息的字典
# print(model.get_config())
# 构建学习流程 optimizer = 优化器，loss = 损失函数，metrics = ["准确率”]
# 优化方法：adam 沿着梯度下降的方向计算变量
# 优化目标：以均方差为损失函数
model.compile(optimizer='adam', loss='mse')
# 测试数据与模型的拟合，输入训练模型 epochs 训练次数
# #参数epochs=1000:使用梯度下降法优化损失函数，下降1000次后停止 以 32 个样本为一个 batch 进行迭代
hist = model.fit(x, y, epochs=1000, batch_size=32)
# model.fit 方法返回一个 History 回调，它具有包含连续误差的列表和其他度量的 history 属性。
# print(hist.history)
# 测试预测数据
test = data.iloc[:2, 1:-1]
# print(test)
# print(data.iloc[:2, -1])
# 输入测试数据，输出预测结果
print(model.predict(test))

# 保存模型
saved_out_path = os.path.join(DATA_DIR, 'saved_models/1555630614')
model.save(saved_out_path)
# 存储和处理大容量科学数据设计的文件格式及相应库文件
# model.save("my_model.h5")

# 保存为 JSON 请注意，该表示不包括权重，只包含结构
# json_string = model.to_json()
# 保存为 YAML 请注意，该表示不包括权重，只包含结构
# yaml_string = model.to_yaml()

print('[Info] 存储saved模型完成! {}'.format(saved_out_path))


