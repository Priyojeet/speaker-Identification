from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D, BatchNormalization
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Dropout
from keras.callbacks import ModelCheckpoint
import os

# data collecting and preprossecing
datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen=ImageDataGenerator(rescale=1./255)

train_generator = datagen.flow_from_directory('data/training_data', # path of your trainging dataset
                                                 target_size = (256, 256),
                                                 batch_size = 16,
                                                 class_mode = 'categorical')
valid_generator = test_datagen.flow_from_directory('data/test_data', # path of your test dataset
                                            target_size = (256, 256),
                                            batch_size = 16,
                                            class_mode = 'categorical')


#defining the model

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(256, 256, 3)))
model.add(BatchNormalization())

model.add(Conv2D(32, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())

model.add(Dense(64, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))

model.add(Dense(128, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))

model.add(Dense(len(os.listdir("data/test_data")), activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

filepath = "del50t.h5" # saving the entire model
checkpoint = ModelCheckpoint(filepath, monitor = 'acc', verbose = 1, save_best_only = True, mode = 'max') # based on accuracy and the best model


model.fit_generator(
    train_generator,
    steps_per_epoch=400,
    epochs=50,
    validation_data=valid_generator,
    validation_steps=40,
    callbacks = [checkpoint])

