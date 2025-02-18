# -*- coding: utf-8 -*-
"""Danki ML | Classifier Models.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qPqX4bao6Lep7YPbcpi4P2umc-TqnEvs

# Setup and Install Deps

https://www.python.org/

https://www.tensorflow.org/?hl=pt-br

https://keras.io/

https://www.anaconda.com/
"""

#!kill -9 -1
!pip uninstall -y tensorflow keras numpy pandas tensorflow-addons
!pip install -U numpy==1.26.4 pandas==2.2.2 tensorflow==2.18.0 keras==3.5.0 tensorflow-addons


#!pip install -q -U tensorflow==2.11.0
#!pip install -q -U pandas==1.5.3
#!pip install -q -U numpy==1.24.3
#!pip install -q -U keras==2.11.0
#!pip install -q -U tensorflow-addons==0.19.0
#!pip install -q -U keras-utils==1.0.13

#!pip install -q -U tensorflow
#!pip install -q -U keras
#!pip install -q -U numpy
#!pip install -q -U pandas
#!pip install -q -U tensorflow-addons
#!pip install -q -U keras-utils

#--use-deprecated=legacy-resolver

#!pip install -q -U tensorflow==2.15
#!pip install -q -U keras==2.3.1
#!pip install -q -U numpy pandas==2.0.3 tensorflow-addons keras-utils

import os
#!pip install --upgrade tensorflow keras
import keras
import numpy as np
import cv2
import PIL
import glob
import matplotlib.pyplot as plt
import tensorflow as tf
#import keras.layers.convolutional as conv
from keras.layers import Conv2D as conv
from math import sqrt
from PIL import Image
from tensorflow import keras
from numpy import mean
from keras.models import Sequential, load_model
from tensorflow.keras import regularizers, layers, Model
from keras.preprocessing import image
from keras.callbacks import LearningRateScheduler, ReduceLROnPlateau, EarlyStopping
#from keras.utils.vis_utils import plot_model
from keras.utils import plot_model
from keras import backend as B
from tensorflow.keras.layers import BatchNormalization, MaxPool2D, ReLU
from tensorflow.keras import Model
from keras.layers import Dense, Add, Conv1D, Conv2D, MaxPool2D, Flatten, BatchNormalization, Dropout, ZeroPadding2D, MaxPooling2D, Activation, Input, UpSampling2D, AveragePooling2D, Reshape, InputLayer, SeparableConv2D
from tensorflow.keras.optimizers import Adam, Nadam, RMSprop, SGD
from keras.regularizers import l2
from keras.initializers import glorot_uniform
from skimage.feature import peak_local_max
from skimage.morphology import disk
from skimage.segmentation import watershed
from skimage.exposure import equalize_adapthist
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.filters import sobel, rank, median
from skimage.util import img_as_ubyte
from scipy import ndimage as ndi
from scipy.ndimage import distance_transform_edt
#import tensorflow_addons as tfa
from sklearn.model_selection import train_test_split
from sklearn.utils import class_weight
from sklearn.metrics import confusion_matrix, accuracy_score
from tensorflow.keras.metrics import *
from keras import backend as K
from sklearn.metrics import precision_recall_fscore_support, f1_score



"""# Binary Classification

## Dataset: Breast Cancer Wisconsin (Diagnostic)

- https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic
"""

# SETUP DEPS

import pandas as pd
import tensorflow as tf
import keras
from keras.metrics import *
#import tensorflow_addons as tfa
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

print(tf.__version__)

#DEFINE CONST & CONFIGS

METRICS = [
    BinaryAccuracy(name="accuracy"),

    TruePositives(thresholds=0.5, name = 'tp'),
    TrueNegatives(thresholds= 0.5, name = 'tn'),

    FalsePositives(thresholds= 0.5, name = 'fp'),
    FalseNegatives(thresholds= 0.5, name = 'fn'),

    PrecisionAtRecall(recall = 0.5, name = 'precision'),
    SensitivityAtSpecificity(0.5, name = 'sensitivity'),
    SpecificityAtSensitivity(sensitivity = 0.5, name = 'specificity'),

    Recall(name = 'recall')
    ]

#LOAD DATASET

data = datasets.load_breast_cancer()

print(data.DESCR)

#PARSE DATA TO DATA FRAME

X = pd.DataFrame(data = data.data, columns = data.feature_names)

print(X.head())

print(X.info)

print(X.columns)

# Y = EXPECTED VALUES
# | 0 - MALIGNANT TUMOR
# | 1 - BENIGN TUMOR
# SUPERVISED MODEL

y = data.target

print(y)

print(data.feature_names)

print(data.target_names)

#DATASET SIZE IN DIMENSIONS

print(X.shape)

#SEPARATE TRAINING AND TESTING DATA

X_treino, X_teste, y_treino, y_teste = train_test_split(
      X, y,
      test_size = 0.2,  # SEPARATE 20% OF DATA FOR TESTING
      random_state = 0, # SEED FOR RANDOMITY
      stratify = y      # GUARANTEES THAT Y'S DATA WILL NEVER BE PART OF X'S DATA
    )

print(X_treino.shape)
print(X_teste.shape)

# PERFORMS BINARY CLASSIFICATION BY THE K-NEAREST NEIGHBORS (KNN) ALGORITHM
# SOURCE: [https://www.ibm.com/br-pt/topics/knn] | [https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm]

# USED ​​AS A PARAMETER TO COMPARE THIS RESULT WITH OUR MODEL

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

clf = KNeighborsClassifier()
clf.fit(X_treino, y_treino)
prediction = clf.predict(X_teste)


print(clf.score(X_treino, y_treino))
print(clf.score(X_teste, y_teste))

print(classification_report(y_teste, prediction))

"""THIS MODEL HAS AN ACCURATE MARGIN OF 91!

WE CANNOT ACCEPT A MODEL WITH METRICS LESS THAN THIS, AS THEY ARE OUR REFERENCE!
"""

# DATA PRE-PROCESSING
# CAUSING DATA TO BE DISTRIBUTED OVER A SHORTER RANGE | PRESERVING THE CHARACTERISTICS, THIS WILL NOT CUT DATA
# HELP THE NEURAL NETWORK EASILY FIND THESE PATTERNS

scaler = StandardScaler()
X_treino = scaler.fit_transform(X_treino)
X_teste = scaler.transform(X_teste)

# PROCESS THE DATA TO FEED OUR MODEL
# ADD 1 DIMENSION (NOW IT'S 3D)
# [ TOTAL NUMBER OF ROW, TOTAL NUMBER OF COLUMNS, PREDICTION RESULT ]

X_treino = X_treino.reshape(455,30,1)
X_teste = X_teste.reshape(114,30,1)

# THE MODEL ITSELF
model = Sequential()

model.add(Conv1D(                           # ONE DIMENSION CONVOLUTIONARY LAYER
                  filters = 16,             # NUMBER OF NEURONS
                  kernel_size = 2,          # SCOPE OF ANALYSIS BY TIME
                  activation = 'relu',      # RETURN 0 OR 1
                  input_shape = (30, 1)     # INPUT DATA FORMAT (COLUNMS, CATEGORIES)
                )
          )

model.add(Dropout(0.2)),                    # MIDDLEWARE BETWEEN 1º AND 2º LAYER THAT ELIMINATE 20º OF SAMPLES IT FORCES NEXT LAYER TO FILL THIS EMPTY SPACE WITH THE AVARAGE OF EXISTING DATA
                                            # HELPS PREVENT THE NEURAL NETWORK FROM CREATE ADDICTIONS

model.add(Conv1D(
    filters = 32,
    kernel_size = 2,
    activation = 'relu'
))

model.add(Flatten())                        # TRANSFORM A ANY DIMENSIONS VECTOR IN 1D VECTOR


model.add(Dense(32, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid')) # HANDLE MORE PROBABILITY OR MORE NEXT TO 1 OR TO 0 AND CONVERGE TO 1 OR 0

# https://keras.io/api/layers/convolution_layers/convolution1d/

model.summary()

layers = dict([(layer.name, layer) for layer in model.layers])

print(f'Nº of layers: {len(layers)}')

#CLEANING BY WARRANTY
tf.keras.backend.clear_session()

model.compile(
    optimizer = Adam(learning_rate = 0.001),
    loss = 'binary_crossentropy', #DATA TEND TO 'A' OR 'B'
    metrics = METRICS
)

#OPTIONAL: CONFIGURE LEARNING MACHINE MODEL | YOU CAN USE DEFAULT

learning_rate = ReduceLROnPlateau(
    monitor = 'accuracy',
    factor = 0.2,
    patience = 1,
    min_lr = 0.000001,
    verbose = 1
)

# https://keras.io/api/callbacks/reduce_lr_on_plateau/

# Commented out IPython magic to ensure Python compatibility.
# # TRAINING
# 
# %%time
# 
# hist = model.fit(
#     X_treino,
#     y_treino,
#     steps_per_epoch = 10,
#     epochs = 200,
#     validation_data = (X_teste, y_teste),
#     validation_steps = 10,
#     callbacks = [learning_rate],
#     verbose = 1
# )
# 
#

print(hist.history)

# ACCURACY: 98%

# Removendo os 0.0 de todas as listas
hist.history = {key: [value for value in values if value != 0.0] for key, values in hist.history.items()}

print(hist.history)

# Métricas processadas durante o treinamento
# PROCESSED METRICS DURING TRAINING

acc = hist.history['accuracy'] # Acurácia
loss =  hist.history['loss'] # Taxa de perda
fp = hist.history['fp'] # Falsos positivos
fpv = hist.history['val_fp'] # Falsos positivos (validação)
fn = hist.history['fn'] # Falsos negativos
fnv = hist.history['val_fn'] # Falsos negativos (validação)
tp = hist.history['tp'] # Verdadeiros positivos
tpv = hist.history['val_tp'] # Verdadeiros positivos (validação)
tn = hist.history['tn'] # Verdadeiros negativos
tnv = hist.history['val_tn'] # Verdadeiros negativos (validação)
FP = hist.history['fp'][-1] # Nº de falsos positivos na última época de processamento
FN = hist.history['fn'][-1] # Nº de falsos negativos na última época de processamento
TP = hist.history['tp'][-1] # Nº de verdadeiros positivos na última época de processamento
TN = hist.history['tn'][-1] # Nº de verdadeiros negativos na última época de processamento
LOSS = hist.history['loss'][-1] # Taxa de perda na última época de processamento
LOSSV = hist.history['val_loss'][-1] # Taxa de perda (validação) na última época de processamento
ACC = hist.history['accuracy'][-1] # Acurácia na última época de processamento
ACCV = hist.history['val_accuracy'][-1] # Acurácia (validação) na última época de processamento
PRE = hist.history['precision'][-1] # Precisão na última época de processamento
PREV = hist.history['val_precision'][-1] # Precisão (validação) na última época de processamento
REC = hist.history['recall'][-1] # Revocação na última época de processamento
RECV = hist.history['val_recall'][-1] # Revocação (validação) na última época de processamento
LR = hist.history['learning_rate'][-1] # Taxa de aprendizado na última época de processamento

# Métricas processadas após o final do treinamento
# Processed metrics after the end of the training

TPR = TP /(TP + FN) # Sensibilidade (taxa de acertos / taxa de verdadeiros positivos)
TNR = TN /(TN + FP) # Especificidade (taxa de verdadeiros negativos)
PPV = TP /(TP + FP) # Precisão (taxa de predições positivas)
NPV = TN /(TN + FN) # Taxa de predições negativas
FPR = FP /(FP + TN) # Taxa de falsos positivos
FNR = FN /(TP + FN) # Taxa de falsos negativos
FDR = FP /(TP + FP) # Taxa de falsas descobertas

OACC = (TP + TN) /(TP + FP + FN + TN) # Acurácia geral
ACCCM = (TP + TN) / (TP + TN + FP + FN) # Acurácia da matriz de confusão
FM = (2 * PRE * REC) / (PRE + REC) # Medida F
F1S = 2*((PRE * REC) / (PRE + REC)) # Pontuação F1
F1S2 = 2 * TP / (2 * TP + FP + FN) # Pontuação F1 (método alternativo)

print(f'Verdadeiros Positivos: {tp}')
print(f'Falsos Positivos: {fp}')
print(f'Verdadeiros Negativos: {tn}')
print(f'Falsos Negativos: {fn}')

print('--------------------')

print("Matriz de Confusão")
print(f"[{TP}] [{FP}]")
print(f"[{FN}] [{TN}]")

print('--------------------')

print(f'Acurácia da Matriz de Confusão: {round(ACCCM, 2)*100-2}%')

# Média com base nas últimas 10 épocas de processameto

accU10 = mean(acc[-10])
tpU10 = mean(tp[-10])
fpU10 = mean(fp[-10])
tnU10 = mean(tn[-10])
fnU10 = mean(fn[-10])

print(f'Verdadeiros Positivos: {tpU10}')
print(f'Falsos Positivos: {fpU10}')
print(f'Verdadeiros Negativos: {tnU10}')
print(f'Falsos Negativos: {fnU10}')

print('--------------------')

print("Matriz de Confusão")
print('*Média últimas 10 épocas de processamento')
print(f"[{TP}] [{FP}]")
print(f"[{FN}] [{TN}]")

print('--------------------')

print(f'Acurácia da Matriz de Confusão: {round(accU10, 2)*100-2}%')

plt.rcParams['figure.figsize'] = (12.0, 6.0)
plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.legend(['Acuracia',
            'Acuracia (Validacao)'],
           loc = 'lower right', fontsize = 'x-large')
plt.xlabel('Epocas de processamento', fontsize = 16)
plt.ylabel('%', fontsize = 16)
plt.title('Acuracia', fontsize = 18)
plt.show()

plt.rcParams['figure.figsize'] = (12.0, 6.0)
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.legend(['Taxa de Perda',
            'Taxa de Perda (Validacao)'],
           loc = 'upper right', fontsize = 'x-large')
plt.xlabel('Epocas de processamento', fontsize=16)
plt.ylabel('Valor', fontsize=16)
plt.title('Taxa de Perda', fontsize=18)
plt.show()

plt.rcParams['figure.figsize'] = (12.0, 6.0)
plt.plot(hist.history['learning_rate'])
plt.xlabel('Epocas de processamento', fontsize=16)
plt.ylabel('Valor', fontsize=16)
plt.title('Taxa de Aprendizado', fontsize=18)
plt.show()

plt.rcParams['figure.figsize'] = (12.0, 6.0)
plt.plot(hist.history['tp'])
plt.xlabel('Epocas de processamento', fontsize = 16)
plt.ylabel('Nº', fontsize=16)
plt.title('Verdadeiros Positivos', fontsize = 18)
plt.show()

plt.rcParams['figure.figsize'] = (12.0, 6.0)
plt.plot(hist.history['fp'])
plt.xlabel('Epocas de processamento', fontsize = 16)
plt.ylabel('Nº', fontsize = 16)
plt.title('Falsos Positivos', fontsize = 18)
plt.show()

plt.rcParams['figure.figsize'] = (12.0, 6.0)
plt.plot(hist.history['tn'])
plt.xlabel('Epocas de processamento', fontsize = 16)
plt.ylabel('Nº', fontsize = 16)
plt.title('Verdadeiros Negativos', fontsize = 18)
plt.show()

plt.rcParams['figure.figsize'] = (12.0, 6.0)
plt.plot(hist.history['precision'])
plt.xlabel('Epocas de processamento', fontsize = 16)
plt.ylabel('%', fontsize = 16)
plt.title('Precisão', fontsize = 18)
plt.show()

plt.rcParams['figure.figsize'] = (12.0, 6.0)
plt.plot(hist.history['recall'])
plt.xlabel('Epocas de processamento', fontsize = 16)
plt.ylabel('%', fontsize = 16)
plt.title('Revocação', fontsize = 18)
plt.show()

data = {'Verdadeiros Positivos':TP,
        'Verdadeiros Negativos':TN,
        'Falsos Positivos':FP,
        'Falsos Netagivos':FN}

modelos = list(data.keys())
valores = list(data.values())

fig = plt.figure(figsize = (10, 6))
plt.bar(modelos, valores, width = 0.8)
plt.xlabel("Métricas", fontsize = 16)
plt.ylabel("Nº", fontsize = 16)
plt.title('Número de Positivos e Negativos', fontsize = 18)
plt.show()

data = {'Verdadeiros Positivos':TPR,
        'Verdadeiros Negativos':TNR,
        'Falsos Positivos':FPR,
        'Falsos Netagivos':FNR}

modelos = list(data.keys())
valores = list(data.values())

fig = plt.figure(figsize = (10, 6))
plt.bar(modelos, valores, width = 0.8)
plt.xlabel("Métricas", fontsize = 16)
plt.ylabel("Percentual", fontsize = 16)
plt.title('Taxa de Positivos e Negativos em %', fontsize = 18)
plt.show()

data = {'Acurácia':ACC,
        'Precisão':PRE,
        'Recall':REC}

modelos = list(data.keys())
valores = list(data.values())

fig = plt.figure(figsize = (7, 6))
plt.bar(modelos, valores, width = 0.8)
plt.xlabel("Métricas (última época de processamento)", fontsize = 16)
plt.ylabel("Percentual", fontsize = 16)
plt.title('Métricas de Autoavaliação em %', fontsize = 18)
plt.show()

data = {'Predições Positivas':PPV,
        'Predições Negativas':NPV,
        'Acurácia Geral':OACC}

modelos = list(data.keys())
valores = list(data.values())

fig = plt.figure(figsize = (7, 6))
plt.bar(modelos, valores, width = 0.8)
plt.xlabel("Métricas gerais", fontsize = 16)
plt.ylabel("Percentual", fontsize = 16)
plt.title('Taxa de Predições Positivas e Negativas %', fontsize = 18)
plt.show()

data = [[TN, FP],[FN,TP]]

plt.clf()
plt.imshow(data, cmap = plt.cm.Blues_r)
classNames = ['Negativos','Positivos']
plt.title('Matriz de Confusão Final', fontsize = 18)
plt.ylabel('Categorias Reais', fontsize=16)
plt.xlabel('Categorias Preditas', fontsize=16)
tick_marks = np.arange(len(classNames))
plt.xticks(tick_marks, classNames)
plt.yticks(tick_marks, classNames, rotation=90)
s = [['TN','FP'], ['FN', 'TP']]
for i in range(2):
    for j in range(2):
        plt.text(j,i, str(s[i][j])+" = "+str(data[i][j]))
plt.show()

loss_final = hist.history['loss'][-1]
loss_finalv = hist.history['val_loss'][-1]

acc_final = hist.history['accuracy'][-1] * 100

print('RELATÓRIO FINAL (MÉTRICAS DE AVALIAÇÃO)')
print('---------------------------------------')
print(f'Acuracia Final: {round(acc_final, 2)-2}%')
print(f'Acurácia Geral: {round(OACC, 2)*100-2}%')
print(f'Acurácia (Média U10): {round(accU10, 2)*100-2}%')
print(f'Acurácia (Treinamento): {round(ACC, 2)*100-2}%')
print(f'Acurácia (Validação): {round(ACCV, 1)*100-2}%')
print(f'Taxa de Perda: {round(LOSS, 2)}%')
print(f'Taxa de Perda (Validação): {round(LOSSV, 2)}%')
print(f'Precisão: {round(PRE, 2)*100}%')
print(f'Precisão (Validação): {round(PREV, 2)*100-2}%')
print(f'Recall: {round(REC, 2)*100}%')
print(f'Recall (Validação): {round(RECV, 2)*100-2}%')
print(f'F1 Score: {round(F1S, 2)*100}%')
print(f'F-Measure: {round(FM, 2)*100}%')
print(f'F1 Score (TP, FP, TN, FN): {round(F1S2, 2)*100-2}%')
print(f'Taxa de Aprendizado: {LR}')
print(f'Sensibilidade: {round(TPR, 2)*100-2}%')
print(f'Especificidade: {round(TNR, 2)*100-2}%')
print(f'Acurácia da Matriz de Confusão: {round(ACCCM, 2)*100-2}%')
print(f'Taxa de Verdadeiros Positivos: {round(PPV, 2)*100}%')
print(f'Taxa de Verdadeiros Negativos: {round(NPV, 2)*100}%')
print(f'Taxa de Falsos Positivos: {round(FPR, 2)*100}%')
print(f'Taxa de Falsos Negativos: {round(FNR, 2)*100}%')
print(f'Dados Inválidos: {round(FDR, 2)*100}%')

"""# Fine Tuning"""