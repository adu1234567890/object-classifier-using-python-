from sklearn.svm import LinearSVC
import numpy as np
import cv2 as cv
from PIL import Image

class Model:
    
    def __init__(self):
        self.model = LinearSVC()

    def train_model(self, counters):
        img_list = []
        class_list = []

        for i in range(1, counters[0]):
            img = cv.imread(f'1/frame{i}.jpg', cv.IMREAD_GRAYSCALE)
            img = img.flatten()  # Flatten to 1D array
            img_list.append(img)
            class_list.append(1)

        for i in range(1, counters[1]):
            img = cv.imread(f'2/frame{i}.jpg', cv.IMREAD_GRAYSCALE)
            img = img.flatten()  # Flatten to 1D array
            img_list.append(img)
            class_list.append(2)

        img_list = np.array(img_list)
        class_list = np.array(class_list)
        
        self.model.fit(img_list, class_list)
        print("Model successfully trained!")

    def predict(self, frame):
        # Check if 'frame' is a 3D array and contains at least 3 channels
        if len(frame.shape) == 3 and frame.shape[2] == 3:
            # Convert the image from RGB to grayscale
            frame_gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
        else:
            # If the image is already single-channel (grayscale), use it directly
            frame_gray = frame
        
        # Save the grayscale image
        cv.imwrite("frame.jpg", frame_gray)
        
        # Open the image and resize (thumbnail)
        img = Image.open("frame.jpg")
        img.thumbnail((150, 150))
        img.save("frame.jpg")

        # Read the image back in grayscale and flatten it for prediction
        img = cv.imread('frame.jpg', cv.IMREAD_GRAYSCALE)
        img = img.flatten()  # Flatten to 1D array for prediction

        # Perform prediction using the model
        prediction = self.model.predict([img])

        return prediction
