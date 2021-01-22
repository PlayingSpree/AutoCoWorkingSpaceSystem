from os import listdir
from os.path import isdir, isfile

import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from mtcnn.mtcnn import MTCNN
from numpy import asarray
from numpy import expand_dims
from numpy import load
from numpy import savez_compressed
from tensorflow.keras.models import load_model

model_path = 'models/facenet_keras.h5'
model = load_model(model_path)


def extract_face(filename, require_size=(160, 160)):
    img = Image.open(filename)
    img = img.convert('RGB')
    pixels = asarray(img)

    detector = MTCNN()
    results = detector.detect_faces(pixels)
    x1, y1, w, h = results[0]['box']
    x1, y1 = abs(x1), abs(y1)
    x2, y2 = x1 + w, y1 + h

    face = pixels[y1:y2, x1:x2]
    img = Image.fromarray(face)
    img = img.resize(require_size)
    face_array = asarray(img)
    return face_array


def load_face(model, directory):
    faces = []
    for file in listdir(directory):
        path = directory + file
        face = extract_face(path)
        face_emb = emb_face(model, face)
        faces.append(face_emb)
    return faces


def compress_face(model, directory):
    for subdir in listdir(directory):
        X, y = [], []
        path = directory + subdir + '/'
        if not isdir(path):
            continue
        save_name = 'data/emb/' + subdir + '.npz'
        if isfile(save_name):
            continue
        faces = load_face(model, path)
        if len(faces) < 10:
            continue
        names = [subdir for _ in range(len(faces))]
        X.extend(faces)
        y.extend(names)
        savez_compressed(save_name, X, y)


def emb_face(model, face_pixels):
    face_pixels = face_pixels.astype('float32')
    mean, std = face_pixels.mean(), face_pixels.std()
    face_pixels = (face_pixels - mean) / std
    samples = expand_dims(face_pixels, axis=0)
    ypred = model.predict(samples)
    return ypred[0]


def run(data_path):
    compress_face(model, data_path)

run('uploads/user/1/face')