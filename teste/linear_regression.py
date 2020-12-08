#%%
import numpy as np
import cv2
import os
import pandas as pd
# %%
clened_folder = "D:\\Projetos\\Datasets\\data_cleaner\\data\\2. cleaned_example"
img_paths = os.listdir(clened_folder)
img_paths = [os.path.join(clened_folder, img_path) for img_path in img_paths]
cleaned_imgs = [cv2.imread(img, cv2.IMREAD_GRAYSCALE) for img in img_paths]
# %%
train_folder = "D:\\Projetos\\Datasets\\data_cleaner\\data\\1. dirty"
img_paths = os.listdir(train_folder)
img_paths = [os.path.join(train_folder, img_path) for img_path in img_paths]
train_imgs = [cv2.imread(img, cv2.IMREAD_GRAYSCALE) for img in img_paths]
# %%
img_paths[0]
# %%
