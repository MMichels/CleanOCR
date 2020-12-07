import keras
import numpy as np


class AutoEncoderHandler:

    def __init__(self, model_path):
        self.model = keras.models.load_model(model_path)

    def predict(self, img_array):
        img_vec = np.expand_dims(img_array, axis=0)
        predicted = self.model.predict(img_vec)
        predicted = np.squeeze(predicted)

        return predicted
