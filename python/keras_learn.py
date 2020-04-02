from keras.layers.core import Activation, Dense, Dropout
from keras.models import Sequential
from keras.optimizers import SGD
from sklearn.model_selection import train_test_split
from sklearn import datasets


def getData():
    data = datasets.load_diabetes()
    X, Y = data.data, data.target
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.33, random_state=42)
    return [X_train, X_test, Y_train, Y_test]


def createMLP(X_train, X_test, Y_train, Y_test):
    # print(X_train.shape)
    model = Sequential()
    d = [[[10, 64], 'tanh', 0.5], [
        [64, 64], 'tanh', 0.5], [[64, 1], 'sigmoid']]
    for i in d:
        model.add(Dense(input_dim=i[0][0], units=i[0][1]))
        model.add(Activation(i[1]))
        if len(i) == 3:
            model.add(Dropout(i[2]))
    sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='mean_squared_error', optimizer=sgd)
    model.fit(X_train, Y_train, epochs=20, batch_size=16)
    score = model.evaluate(X_test, Y_test, batch_size=16)
    print(score)


data = getData()
createMLP(*data)
