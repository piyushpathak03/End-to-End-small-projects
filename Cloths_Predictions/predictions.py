import os
import tensorflow as tf
import cv2
import numpy as np
from itertools import chain
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model


class Cloths_Classification:
    def __init__(self):
        self.class_names = ['Goggles', 'Hat', 'Jacket', 'Shirt', 'Shoes', 'Shorts', 'T-Shirt', 'Trouser', 'Wallet','Watch']
        self.model = load_model("model/fashion.h5")

    def get_prediction(self, image):
        img = cv2.imread(image)
        dim = (224, 224)
        img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        x = np.array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        preds = self.model.predict(x)
        pred_class = self.class_names[np.argmax(preds[0])]
        return pred_class

    def list_and_delete_previous_files(self):
        self.list_of_files = []
        if os.path.exists('./uploads'):
            self.list_of_files = os.listdir('./uploads')
            print('------list of files------')
            print(self.list_of_files)
            for self.image in self.list_of_files:
                try:
                    print("------Deleting File------")
                    os.remove("./uploads/" + self.image)
                except Exception as e:
                    print('error in deleting:  ', e)
        else:
            print('Folder Does not exist!!')