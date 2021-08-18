from sklearn import datasets
from xgboost import XGBRegressor
from sklearn.datasets import load_boston    
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import r2_score
from sklearn.feature_selection import SelectFromModel

# datasets = load_boston()
# x = datasets.data
# y = datasets.target

x, y = load_boston(return_X_y=True)

# print(x.shape, y.shape)     # (506, 13) (506,)

def model_1():

    x_train, x_test, y_train, y_test = train_test_split(x, y,
                    train_size=0.8, shuffle=True, random_state=66
    )

    model = XGBRegressor(n_jobs=-1)

    model.fit(x_train, y_train)

    score = model.score(x_test, y_test)     
    print("model.score :", score)       # model.score : 0.9221188601856797

def model_2():
    
    x_train, x_test, y_train, y_test = train_test_split(x, y,
                    train_size=0.8, shuffle=True, random_state=66
    )

    model = XGBRegressor(n_jobs=-1)

    model.fit(x_train, y_train)

    thresholds = np.sort(model.feature_importances_)
    print(thresholds)
    # [0.00134153 0.00363372 0.01203115 0.01220458 0.01447935 0.01479119
    # 0.0175432  0.03041655 0.04246345 0.0518254  0.06949984 0.30128643
    # 0.42848358]

    for thresh in thresholds:
        selection = SelectFromModel(model, threshold=thresh, prefit=True)

        select_x_train = selection.transform(x_train)
        select_x_test = selection.transform(x_test)
        # print(select_x_train)

        selection_model = XGBRegressor(n_jobs=-1)
        selection_model.fit(select_x_train, y_train)

        y_predict = selection_model.predict(select_x_test)

        score = r2_score(y_test, y_predict)

        print("Thresh=%.3f, n=%d, R2 : %.2f%%" %(thresh, select_x_train.shape[1],
                score*100
        ))

# model_1()
model_2()
