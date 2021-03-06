import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.metrics import r2_score

# 1. 데이터
datasets = load_diabetes()
x = datasets.data
y = datasets.target

x_train, x_test, y_train, y_test = train_test_split(x, y, 
        train_size=0.75, shuffle=True)

# print(x[:1])
# print(y[:1])
# print(x.shape, y.shape) # (442, 10) (442,)

# print(datasets.feature_names)
# ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']

# print(datasets.DESCR)
# :Attribute Information:
#       - age     age in years - 나이
#       - sex     - 성별
#       - bmi     body mass index - 체질량 지수
#       - bp      average blood pressure - 평균 혈압
#       - s1      tc, T-Cells (a type of white blood cells)
#       - s2      ldl, low-density lipoproteins
#       - s3      hdl, high-density lipoproteins
#       - s4      tch, thyroid stimulating hormone
#       - s5      ltg, lamotrigine
#       - s6      glu, blood sugar level

# print(y[:30])
# print(np.min(y), np.max(y))

# 2. 모델 구성

model = Sequential()
model.add(Dense(96, input_shape=(10,), activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(8, activation='relu'))  
model.add(Dense(4, activation='relu'))           
model.add(Dense(2, activation='relu'))          #활성화 함수
model.add(Dense(1))

# 3. 컴파일, 훈련

model.compile(loss='mse', optimizer='adam')
model.fit(x_train, y_train, epochs=200, validation_split=0.5, batch_size=32, shuffle=False, verbose=2)

# 4. 평가, 예측

loss = model.evaluate(x_test, y_test)
print('loss는 :', loss)

# mse, R2

y_predict = model.predict(x_test)

r2 = r2_score(y_test, y_predict)
print('r2는 :', r2)

'''

loss는 : 3308.3359375
r2는 : 0.5337157987847735

loss는 : 2418.124755859375
r2는 : 0.5710359031333607

loss는 : 3024.7998046875
r2는 : 0.5831950785102884

4/4 [==============================] - 0s 2ms/step - loss: 2257.9578
loss는 : 2257.957763671875
r2는 : 0.6555743360325862


과제 1.
0.62 까지 올릴것!!
'''