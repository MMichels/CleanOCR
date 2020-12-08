import cv2
import numpy as np


class ImageFilterApplier():
    def __init__(self, image):
        self.image = image

    def add(self, image):
        self.image = cv2.add(self.image, image)
        return self.image.copy()

    def subtract(self, image):
        self.image = cv2.subtract(self.image, image)
        return self.image.copy()

    def to_gray_scale(self):
        self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        return self.image.copy()

    def resize(self, size=(540, 420)):
        self.image = cv2.resize(self.image, size)
        return self.image.copy()

    def equalize(self):
        self.image = cv2.equalizeHist(self.image)
        return self.image.copy()

    def border_filter(self):
        """
        mask = np.full((3, 3), -1, np.int)
        mask[1, 1] = 8
        mask
        self.image = cv2.filter2D(self.image, -1, mask)
        """
        self.image = cv2.Laplacian(self.image, cv2.CV_8U)
        return self.image.copy()

    def median_filter(self, intensity=1):
        self.image = cv2.medianBlur(self.image, ksize=intensity)
        return self.image.copy()

    def erode(self, iterations=1):
        structuring_element1 = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 1))
        structuring_element2 = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 2))
        self.image = cv2.erode(self.image, structuring_element1, iterations=iterations)
        self.image = cv2.erode(self.image, structuring_element2, iterations=iterations)
        return self.image.copy()

    def dilate(self, iterations=1):
        structuring_element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        self.image = cv2.dilate(self.image, structuring_element, iterations=iterations)
        return self.image.copy()

    def threshold(self, threshold_level=127):
        self.image = cv2.adaptiveThreshold(self.image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                           cv2.THRESH_BINARY, 11, 2)
        return self.image.copy()
