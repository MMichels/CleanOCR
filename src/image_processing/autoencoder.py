import keras
import numpy as np


class AutoEncoderHandler:

    def __init__(self, model_path):
        self.model = keras.models.load_model(model_path)

    def predict(self, image):
        img_array = keras.preprocessing.image.img_to_array(image)
        img_array = img_array.astype("float32")/255.
        img_vec = np.expand_dims(img_array, axis=0)
        predicted = self.model.predict(img_vec)
        predicted = np.squeeze(predicted) * 255

        return predicted.astype("uint8")
