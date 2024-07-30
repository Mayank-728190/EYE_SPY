import tkinter as tk 
from tkinter import filedialog
import cv2
import numpy as np 
from PIL import Image, ImageTk

def detect_faces(image_path):
    def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
            cv2.putText(img, text, (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
        return img

    faceCascade = cv2.CascadeClassifier("lbpcascade_frontalface_opencv.xml")

    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Resize the image to fit within a specific size limit while maintaining aspect ratio
    max_height = 600
    max_width = 800
    height, width, _ = img.shape
    if height > max_height or width > max_width:
        ratio = min(max_height / height, max_width / width)
        img = cv2.resize(img, (int(width * ratio), int(height * ratio)))

    img = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face")

    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    panel = tk.Label(window, image=img)
    panel.image = img
    panel.grid(row=1, column=0, padx=10, pady=10)

def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        detect_faces(file_path)

window = tk.Tk()
window.title("Face recognition system")

upload_button = tk.Button(window, text="Upload Image", font=("Algerian", 20), bg='blue', fg='white', command=upload_image)
upload_button.grid(row=0, column=0, padx=10, pady=10)

window.mainloop()
