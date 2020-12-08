# %%
import cv2


# %%
file = "D:\\Projetos\\Python\\projetos\\CleanOCR\\resources\\1.dirty/12.png"
def cv2_imshow(imagem):
    cv2.imshow("imagem", imagem)
    cv2.waitKey()
    cv2.destroyAllWindows()


# %%
img = cv2.imread(file)
cv2_imshow(img)


# %%
background = cv2.medianBlur(img, 21)
cv2_imshow(background)

# %%
t = cv2.subtract(background, img)
t = cv2.bitwise_not(t)
cv2_imshow(t)

#%%
borders = cv2.Laplacian(t, cv2.CV_8UC1)
cv2_imshow(borders)

# %%
ee = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

# %%
dilated = cv2.erode(t, ee)
cv2_imshow(dilated)
# %%

f = cv2.subtract(dilated, borders)
cv2_imshow(f)
# %%
