from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt

#1. 데이터
x_train = np.array([1, 2, 3, 4, 5, 6, 7]) # 훈련, 공개하는 것
y_train = np.array([1, 2, 3, 4, 5, 6, 7])
x_test = np.array([8, 9, 10])             # 평가하는 것 
y_test = np.array([8, 9, 10])
x_val = np.array([11,12,13])              # 
y_val = np.array([11,12,13])


#2. 모델 구성
model = Sequential()
model.add(Dense(4, input_dim=1))
model.add(Dense(10))
model.add(Dense(10))
model.add(Dense(1))

#3. 컴파일, 훈련 
model.compile(loss='mse', optimizer='adam')

model.fit(x_train, y_train, epochs=1000, batch_size=1, validation_data=(x_val, y_val))

#4. 평가, 예측 
loss = model.evaluate(x_test, y_test)
print('loss : ', loss)

#result = model.predict([12])
#print('result :', result)

y_predict = model.predict([11])


# plt.scatter(x, y)
# plt.plot(x, y_predict, color='red')
# plt.show()

'''

Epoch 1000/1000
10/10 [==============================] - 0s 556us/step - loss: 4.5764
1/1 [==============================] - 0s 70ms/step - loss: 3.2734
loss :  3.2733566761016846
result : [[10.884739]]

'''
