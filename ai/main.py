import tensorflow as tf
from tensorflow import keras

import numpy as np

def buildModel():
    """
    Build the model
    """
    model = keras.Sequential()


    model.add(keras.layers.Dense(64, activation='relu', input_dim=4))
    model.add(keras.layers.Dropout(0.1))
    model.add(keras.layers.Dense(32, activation='relu'))
    model.add(keras.layers.Dropout(0.1))
    model.add(keras.layers.Dense(2, activation='softmax'))


    model.compile(optimizer=tf.keras.optimizers.Adam(),
                loss='categorical_crossentropy',
                metrics=['accuracy'])

    model.summary()

    return model

def loadData():
    """
    Loads the training data from the dataset
    """
    data = np.loadtxt(open("log.csv", "rb"), delimiter=",", skiprows=1)
    print(data[:,:-1])
    inputData = data[:,:-1]
    outputData = data[:,-1:]
    outputData = keras.utils.to_categorical(outputData)
    print(inputData)
    print(outputData)

    return inputData, outputData

def trainModel(model, data, labels):
    model.fit(data, labels, epochs=300, batch_size=256)

def main():
    model = buildModel()
    data, labels = loadData()
    trainModel(model, data, labels)

    filepath = 'model.tfmodel'

    tf.keras.models.save_model(
        model,
        filepath,
        overwrite=True,
        include_optimizer=True
    )


main()