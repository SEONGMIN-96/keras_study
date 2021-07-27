from tensorflow.keras import datasets
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import reuters
import numpy as np
import pandas as pd

(x_train, y_train), (x_test, y_test) = reuters.load_data(
        num_words=100, test_split=0.2
)      #num_words=N -> 빈도순위가 1~N순위인 단어만 사용, 모든 순위는 None  

print(x_train[0],type(x_train[0]))
print(x_train[1],type(x_train[0]))

print(len(x_train[0]), len(x_train[1]))

# print(x_train[0].shape) AttributeError: 'list' object has no attribute 'shape'

print(x_train.shape, x_test.shape) # (8982,) (2246,)
print(y_train.shape, y_test.shape) # (8982,) (2246,)

print(type(x_train)) # <class 'numpy.ndarray'>

print("뉴스기사의 최대길이 :", max(len(i) for i in x_train))
# 뉴스기사의 최대길이 : 2376
print("뉴스기사의 평균길이 :", sum(map(len, x_train)) / len(x_train))
# 뉴스기사의 평균길이 : 145.5398574927633

plt.hist([len(s) for s in x_train], bins=50)
# plt.show()

# 전처리

from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical

x_train = pad_sequences(x_train, maxlen=100, padding='pre')     # (8982, 100)
x_test = pad_sequences(x_test, maxlen=100, padding='pre')       # (2246, 100)
print(x_train.shape, x_test.shape)  
print(type(x_train[0]), type(x_test[0])) # <class 'list'> <class 'numpy.ndarray'>
print(np.unique(x_train))
print(x_train[1])

# y 확인

print(np.unique(y_train)) # 0~45

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

print(y_train.shape, y_test.shape) # (8982, 46) (2246, 46)

# 2. 모델 구성
# 실습, 완성해보세요!!

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding

model = Sequential()
model.add(Embedding(100, 64))
model.add(LSTM(32))
model.add(Dense(64))
model.add(Dense(46, activation='softmax'))

model.summary()

# 3. 컴파일, 훈련

from tensorflow.keras.callbacks import EarlyStopping
import time

es = EarlyStopping(monitor='val_loss', mode='min', patience=10)

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])

start_time = time.time()
model.fit(x_train, y_train, epochs=100, batch_size=512, validation_split=0.2, verbose=1,
                callbacks=[es])
end_time = time.time() - start_time

# 4. 평가, 예측

loss = model.evaluate(x_test, y_test)

print('loss :', loss[0])
print('acc :', loss[1])
print('소요 시간:', end_time)
