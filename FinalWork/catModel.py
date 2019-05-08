from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import RMSprop     # 优化函数
import matplotlib.pyplot as plt
from data_loader import cat_data_loader  # 数据集读取接口


class myCallback(keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if logs.get('loss') < 0.55:       # 损失小于0.55就停止
            print("\nLoss is low so cancelling training")
            self.model.stop_training = True


class CatModel:
    """
    猫咪训练模型
    """
    def __init__(self):
        self.callbacks = myCallback()  # 召回用
        (self.x_train, self.y_train), (self.x_test, self.y_test) = cat_data_loader()

        # print(self.x_train.shape)
        # print(self.x_test.shape)
        # print(self.y_train.shape)
        # print(self.y_test.shape)
        # index = 20
        # self.show_image(index)
        self.cat_model()

    def cat_model(self):
        x_train_flatten = self.x_train.reshape(self.x_train.shape[0], -1)
        x_test_flatten = self.x_test.reshape(self.x_test.shape[0], -1)

        # print(x_train_flatten.shape)
        # print(x_test_flatten.shape)
        self.x_train = x_train_flatten / 255
        self.x_test = x_test_flatten / 255

        cat_model = Sequential()
        cat_model.add(Dense(512, activation="relu", input_shape=(30000,)))  # 100x100x3
        cat_model.add(Dense(256, activation="relu"))
        cat_model.add(Dense(128, activation="relu"))
        cat_model.add(Dense(64, activation="relu"))
        cat_model.add(Dense(32, activation="relu"))
        cat_model.add(Dense(1, activation="sigmoid"))

        print(cat_model.summary())
        cat_model.compile(optimizer=RMSprop(lr=1e-4), loss="binary_crossentropy", metrics=["accuracy"])

        cat_model.fit(self.x_train, self.y_train,
                      epochs=20,
                      validation_data=(self.x_test, self.y_test),
                      callbacks=[self.callbacks])

        cat_model.save("./cats_and_dogs/cat.h5")   # 保存模型

    def show_image(self, index):

        plt.imshow(self.x_train[index])  # 显示图片


if __name__ == "__main__":
    CatModel()
