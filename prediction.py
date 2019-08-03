import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import matplotlib.pyplot as plt
from matplotlib.image import imread
import os


def make_pred():
	# create a list according to your data_directory and the order must be same.
	column = os.listdir("data/test_data")
	new_model = load_model('dell1.h5')
	test_image = image.load_img("test.png", target_size = (256, 256, 3))
	test_image = image.img_to_array(test_image)
	test_image = test_image/225
	result = new_model.predict(test_image.reshape(1, 256, 256, 3))
	pred_bool = (result >0.5)
	predictions = pred_bool.astype(int)
	for i in predictions:
	    d = dict(zip(column, i))
	final_prediction = [key  for (key, value) in d.items() if value == 1]
	name = ""
	for i in final_prediction:
		for j in i:
			name+=j
	return name

#print(make_pred())