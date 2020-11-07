#%%
import numpy as np
import matplotlib.pyplot as plt
import cv2
import time

from os import listdir
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Normalizer
from skimage.transform import resize
from PIL import Image
from tensorflow.keras.models import load_model
from numpy import load, asarray, expand_dims


#%%
model_path = 'models/facenet_keras.h5'
model = load_model(model_path)

#%%
cascade_path = 'haarcascade_frontalface_default.xml'
cascade = cv2.CascadeClassifier(cascade_path)


#%%
def emb_face(model, face_pixels):
    face_pixels = face_pixels.astype('float32')
    mean, std = face_pixels.mean(), face_pixels.std()
    face_pixels = (face_pixels - mean) / std

    samples = expand_dims(face_pixels, axis=0)
    ypred = model.predict(samples)
    return ypred


def load_userface(directory):
    trainX, trainy = [], []
    for filename in listdir(directory):
        path = directory + filename
        data = load(path)
        trainX.extend(data['arr_0'])
        trainy.extend(data['arr_1'])
    return asarray(trainX), asarray(trainy)


#%%
trainX, trainy = load_userface('data/')
in_enc = Normalizer(norm='l2')
trainX = in_enc.transform(trainX)

out_enc = LabelEncoder()
out_enc.fit(trainy)
trainy = out_enc.transform(trainy)

clf = SVC(kernel='linear', probability=True)
clf.fit(trainX, trainy)


#%%
vc = cv2.VideoCapture(0)
i = 0
before_pred = None
door_lock = True

while True:
    is_capturing, frame = vc.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = cascade.detectMultiScale(frame,
                                    scaleFactor=1.1,
                                    minNeighbors=3,
                                    minSize=(100, 100))
    pred = None
    if len(faces) != 0:
        face = faces[0]
        (x1, y1, w, h) = face
        x2, y2 = x1 + w, y1 + h
        img = resize(frame[y1:y2, x1:x2], (160, 160), mode='reflect')
        face_pixels = asarray(img)
        embs = emb_face(model, face_pixels)
        embs = in_enc.transform(embs)
        pred = out_enc.inverse_transform(clf.predict(embs))
        cv2.rectangle(frame,
                    (x1, y1),
                    (x2, y2),
                    (255, 0, 0),
                    thickness=2)
        #print(pred)
    if pred == before_pred and pred != None:
        print(pred)
        i += 1
    else:
        i = 0

    before_pred = pred
    pred = None
    print(i)
    if i == 30:
        i = 0
        door_lock = False
        print('Unlocked!')
        time.sleep(5)
        print('Loced!')

    door_lock = True
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vc.release()
cv2.destroyAllWindows()
