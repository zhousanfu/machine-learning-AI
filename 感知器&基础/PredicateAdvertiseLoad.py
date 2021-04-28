# -*- coding:utf-8 -*-
# 从保存的模型重新加载新的 keras 模型
import tensorflow as tf
import pandas as pd

data = pd.read_csv("Advertising.csv")
test = data.iloc[:1, 1:-1]

# 重新实例化模型
model = tf.keras.models.load_model("saved_models/1555630614")
model.summary()

print(model.predict(test))

