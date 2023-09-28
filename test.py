import cv2
from PIL import ImageTk, Image
file_path="30ins.png"
img = cv2.imread(file_path,cv2.IMREAD_COLOR)
img=cv2.resize(img,(30,30))
print(img.shape)