import numpy as np
from sklearn import datasets
from sklearn.datasets import load_iris

# 1. 데이터

datasets = load_iris()
# print(datasets.DESCR)
# print(datasets.feature_names)

x = datasets.data
y = datasets.target

# 1

from tensorflow.keras.utils import to_categorical

# y = to_categorical(y)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, 
                                train_size=0.8, shuffle=True, random_state=94)

# 1_1. 데이터 전처리

from sklearn.preprocessing import QuantileTransformer

# scaler = QuantileTransformer()
# scaler.fit(x_train)
# scaler.transform(x_train)
# scaler.transform(x_test)

# 2. 모델 구성
# 머신러닝은 기존의 딥러닝의 방식과는다르게 파라미터 튜닝과정이 없음

from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Input
from sklearn.svm import LinearSVC, SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# tree 구조 확장 -> RandomForest

# LogisticRegression -> 분류모델

# model = LinearSVC()
# model.score :  0.9333333333333333
# accuracy_score :  0.9333333333333333

# model = LogisticRegression()
# model.score :  1.0
# accuracy_score :  1.0

# model = SVC()
# model.score :  1.0
# accuracy_score :  1.0

# model = KNeighborsClassifier()
# model.score :  1.0
# accuracy_score :  1.0

# model = DecisionTreeClassifier()
# model.score :  1.0
# accuracy_score :  1.0

# model = RandomForestClassifier()
# model.score :  1.0
# accuracy_score :  1.0


# 3. 컴파일, 훈련

# 3_1. EarlyStopping

from tensorflow.keras.callbacks import EarlyStopping

es = EarlyStopping(monitor='val_loss', mode='min', patience=20)

# 컴파일 및 핏 과정도 변경됨

model.fit(x_train, y_train)
# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# model.fit(x_train, y_train, epochs=1000, batch_size=8, verbose=1, shuffle=True, validation_split=0.2, callbacks=es)

# 평가, 예측
# 기존의 evaluate -> model.score

results = model.score(x_test, y_test)
print("model.score : ",results)
# loss = model.evaluate(x_test, y_test)
# print('loss는 :', loss[0])
# print('accuracy는 :', loss[1])

from sklearn.metrics import r2_score, accuracy_score

y_predict = model.predict(x_test)
acc = accuracy_score(y_test, y_predict)
print("accuracy_score : ", acc)

# model.score = accuracy_score


