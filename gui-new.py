import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import cv2
import numpy

from keras.models import load_model
model = load_model('traffic_classifier.h5')
print(model.summary)

classes = {1: 'Speed limit (20km/h)',
           2: 'Speed limit (30km/h)',
           3: 'Speed limit (50km/h)',
           4: 'Speed limit (60km/h)',
           5: 'Speed limit (70km/h)',
           6: 'Speed limit (80km/h)',
           7: 'End of speed limit (80km/h)',
           8: 'Speed limit (100km/h)',
           9: 'Speed limit (120km/h)',
           10: 'No passing',
           11: 'No passing veh over 3.5 tons',
           12: 'Right-of-way at intersection',
           13: 'Priority road',
           14: 'Yield',
           15: 'Stop',
           16: 'No vehicles',
           17: 'Veh > 3.5 tons prohibited',
           18: 'No entry',
           19: 'General caution',
           20: 'Dangerous curve left',
           21: 'Dangerous curve right',
           22: 'Double curve',
           23: 'Bumpy road',
           24: 'Slippery road',
           25: 'Road narrows on the right',
           26: 'Road work',
           27: 'Traffic signals',
           28: 'Pedestrians',
           29: 'Children crossing',
           30: 'Bicycles crossing',
           31: 'Beware of ice/snow',
           32: 'Wild animals crossing',
           33: 'End speed + passing limits',
           34: 'Turn right ahead',
           35: 'Turn left ahead',
           36: 'Ahead only',
           37: 'Go straight or right',
           38: 'Go straight or left',
           39: 'Keep right',
           40: 'Keep left',
           41: 'Roundabout mandatory',
           42: 'End of no passing',
           43: 'End no passing veh > 3.5 tons'}


top = tk.Tk()
top.geometry('900x600')
top.title('Traffic sign classification')
top.configure(background='#000000')

label = Label(top, background='#000000', font=('arial', 15, 'bold'))
sign_image = Label(top, background='#000000')


def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    # image = image.resize((30, 30))
    # image=cv2.imread(file_path, cv2.IMREAD_COLOR) 
    img = cv2.imread(file_path,cv2.IMREAD_COLOR)
    img=cv2.resize(img,(30,30))
    image = numpy.expand_dims(img, axis=0)
    image = numpy.array(image)
    print(image.shape)
    
    pred = model.predict([image])[0]
    p = min(range(len(pred)), key=lambda i: abs(pred[i]-1))
    ans = classes[p+1]
    print(ans)
    label.configure(foreground='#ff0000', text=ans ,font=('Poppins', 30, 'bold'),background='#000000')



def show_classify_button(file_path):
    classify_b = Button(top, text="Classify Image",
                        command=lambda: classify(file_path), padx=10, pady=5)
    classify_b.configure(background='#364156',
                         foreground='white', font=('arial', 10, 'bold'))
    classify_b.place(relx=0.425, rely=0.75)


def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        MAX_SIZE = (1000, 1000)  
        im = ImageTk.PhotoImage(uploaded)
        

        sign_image.configure(image=im , background='#000000')
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass


upload = Button(top, text="Upload an image",
                command=upload_image, padx=10, pady=5)
upload.configure(background='#364156', foreground='white',
                 font=('arial', 10, 'bold'))

upload.pack(side=BOTTOM, pady=50)
sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)
heading = Label(top, text="------  Know Your Traffic Sign  ------",
                pady=20, font=('Poppins', 20, 'bold'))
heading.configure(background='#000000', foreground='#ffffff')
heading.pack()
top.mainloop()
