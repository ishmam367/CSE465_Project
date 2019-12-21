# -*- coding: utf-8 -*-
"""ANN_Train_Test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mJSBrRmqjaSevQj_8wwuhgqvRPAjyfCh
"""

from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
import numpy as np

dataset=pd.read_csv('liver.csv')
dataset.isnull().sum()
dataset['Albumin_and_Globulin_Ratio'].mean()
dataset=dataset.fillna(0.94)
dataset.head()

X = dataset.drop(['Gender','Dataset'], axis=1)
X.head(3)

X=dataset[['Age', 'Total_Bilirubin', 'Direct_Bilirubin',
       'Alkaline_Phosphotase', 'Alamine_Aminotransferase',
       'Aspartate_Aminotransferase', 'Total_Protiens', 'Albumin',
       'Albumin_and_Globulin_Ratio']]
y=dataset['Dataset']
from sklearn.model_selection import train_test_split


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=123)

model=Sequential()
model.add(Dense(12,input_dim=9,activation='relu'))
model.add(Dense(15,activation='relu'))
model.add(Dense(8,activation='relu'))
model.add(Dense(10,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss="binary_crossentropy",optimizer="adam",metrics=['accuracy'])
model.fit(X_train,y_train,epochs=10,batch_size=10)
scores1=model.evaluate(X_train,y_train)
print("Training Accuracy")
print(model.metrics_names[1],scores1[1]*100)

model.fit(X_test,y_test,epochs=10,batch_size=10)
scores2=model.evaluate(X_test,y_test)

print("Testing Accuracy")
print(model.metrics_names[1],scores2[1]*100)