import os
import cv2 as cv
from PIL import Image
import numpy as np

def getImageAndLabels(path):
    facesSamples = []  # save face data
    ids = []  # save names

    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]  # save info of pictures
    face_detector = cv.CascadeClassifier \
        ('C:/Users/HP/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/'
         'haarcascade_frontalface_alt2.xml')  # load the classifier

    for imagePath in imagePaths:  #
        PIL_img = Image.open(imagePath).convert('L')
        img_numpy = np.array(PIL_img, 'uint8')
        faces = face_detector.detectMultiScale(img_numpy)
        id = int(os.path.split(imagePath)[1].split('.')[0])
        for x, y, w, h in faces:
            ids.append(id)
            facesSamples.append(img_numpy[y:y+h, x:x+w])

    print('id:', id)
    print('fs:', facesSamples)
    return facesSamples, ids


if __name__ == '__main__':
    path = './printscreen'
    faces, ids = getImageAndLabels(path)
    recognizer = cv.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, np.array(ids))
    recognizer.write('trainer.yml')
