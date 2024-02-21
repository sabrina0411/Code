# -*- coding: utf-8 -*-
"""Anti-money.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VBhlIrWnfdNTKIWpu7SqIIHkK5vYTIMo
"""

import pandas as pd
import csv
header = ["type","source", "destination", "numberOfTransaction_from_same_source","amount", "isfraud"]
with open('processed_data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(header)

import pandas as pd
import csv
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

import matplotlib.pyplot as plt
import numpy as np


def plotGraph(y_test, y_pred, regressorName):
    if max(y_test) >= max(y_pred):
        my_range = int(max(y_test))
    else:
        my_range = int(max(y_pred))
    plt.scatter(range(len(y_pred)), y_pred, color='red')
    plt.scatter(range(len(y_test)), y_test, color='black')

    plt.title(regressorName)
    plt.show()
    return

a = pd.read_csv("/content/ML.csv")

a.head()

a.shape

ind = 0
count = 0
for i in list(a['sourceid'])[1:-1]:
  if ind == 0:
    flag = list(a['sourceid'])[0]
  if ind >0:
    if flag == i:
      count +=1
    else:
      file = open('processed_data.csv', 'a', newline='')
      with file:
          writer = csv.writer(file)
          writer.writerow([a['typeofaction'][ind-1],a['sourceid'][ind-1],a['destinationid'][ind],count+1,a['amountofmoney'][ind-1],a['isfraud'][ind-1]])
      print(flag,count+1)
      flag = i
      count = 0
  ind+=1

import pandas as pd
import csv
header = ["type", "numberOfTransaction_for_same_destination", "numberOfTransaction_from_same_source","amount", "isfraud"]
with open('processed_data_2.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(header)

a = pd.read_csv("/content/processed_data.csv")

a.shape

a.head()

ind = 0
count = 0
for i in list(a['destination'])[1:-1]:
  if ind == 0:
    flag = list(a['destination'])[0]
  if ind >0:
    if flag == i:
      count +=1
    else:
      file = open('processed_data_2.csv', 'a', newline='')
      with file:
          writer = csv.writer(file)
          writer.writerow([a['type'][ind-1],count+1,a['numberOfTransaction_from_same_source'][ind],a['amount'][ind-1],a['isfraud'][ind-1]])
      print(flag,count+1)
      flag = i
      count = 0
  ind+=1

a = pd.read_csv("/content/processed_data_2.csv")

a

import pandas as pd
import csv
header = ["type", "numberOfTransaction_for_same_destination", "numberOfTransaction_from_same_source","numberof_sequential_same_ammount", "isfraud"]
with open('processed_data_3.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(header)

a = pd.read_csv("/content/processed_data_2.csv")

ind = 0
count = 0
for i in list(a['amount'])[1:-1]:
  if ind == 0:
    flag = list(a['amount'])[0]
  if ind >0:
    if flag == i:
      count +=1
    else:
      file = open('processed_data_3.csv', 'a', newline='')
      with file:
          writer = csv.writer(file)
          writer.writerow([a['type'][ind-1],a['numberOfTransaction_for_same_destination'][ind],a['numberOfTransaction_from_same_source'][ind],count+1,a['isfraud'][ind-1]])
      print(flag,count+1)
      flag = i
      count = 0
  ind+=1

df = pd.read_csv("/content/processed_data_3.csv")

df.head()

df.shape

target = df.isfraud
target.head()

inputs = df.drop('isfraud', axis='columns')
inputs.head()

dummies = pd.get_dummies(inputs.type)  # get dummy data for type column. ex: 1 means cash-in 0 means transfer
dummies.head()

inputs = pd.concat([inputs, dummies], axis='columns')
inputs = inputs.drop('type', axis='columns')
inputs.head()

target.head()

inputs.head()

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(inputs, target, test_size=0.2)

print(len(x_train), len(x_test), len(y_train), len(y_test))

"""### **Linear Regression**"""

# linear_reg_model = LinearRegression()
# linear_reg_model.fit(x_train, y_train)

# y_pred = linear_reg_model.predict(x_test)
# y_pred

# linear_reg_model.score(x_test, y_pred)

# plotGraph(x_test, y_pred, "linear")

"""### **Support Vactor Machine**"""

from sklearn.svm import SVC
classifier = SVC(kernel='linear', random_state=0)
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)
y_pred

classifier.score(x_test, y_pred)

print(classification_report(y_test, y_pred))

from sklearn.metrics import confusion_matrix
cf_matrix = confusion_matrix(y_test, y_pred)
cf_matrix

import seaborn as sns
# sns.heatmap(cm, annot=True, cbar=False, fmt='g')
sns.heatmap(cf_matrix, annot=True, cbar=False, fmt='g')

loss = history.history['loss']
validation_loss = history.history['val_loss']
accuracy = history.history['accuracy']
validation_accuracy =history.history['val_accuracy']

epochs = range(1, len(loss)+1)

fig1 = plt.figure(figsize=(8,4))
plt.plot(epochs,loss,c="red",label="Training")
plt.plot(epochs,validation_loss,c="blue",label="Validation")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.xticks(epochs)
plt.legend()

epochs1 = range(1, len(accuracy)+1)

fig2 = plt.figure(figsize=(8,4))
plt.plot(epochs1,accuracy,c="red",label="Training")
plt.plot(epochs1,validation_accuracy,c="blue",label="Validation")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.xticks(epochs1)
plt.legend()

# import matplotlib.pyplot as plt
# plot_bar_chart(y_test, y_pred, "SVM")
# # plotGraph(y_test, y_pred, "SVM")

"""### **Random Forest**"""

clf_rf = RandomForestClassifier(n_estimators = 100)
clf_rf.fit(x_train, y_train)

y_pred = clf_rf.predict(x_test)
y_pred

clf_rf.score(x_test, y_pred)

print(classification_report(y_test, y_pred))

from sklearn.metrics import confusion_matrix
cf_matrix = confusion_matrix(y_test, y_pred)
cf_matrix

import seaborn as sns
sns.heatmap(cf_matrix, annot=True, cbar=False, fmt='g')
cf_matrix

loss = history.history['loss']
validation_loss = history.history['val_loss']
accuracy = history.history['accuracy']
validation_accuracy =history.history['val_accuracy']

epochs = range(1, len(loss)+1)

fig1 = plt.figure(figsize=(8,4))
plt.plot(epochs,loss,c="red",label="Training")
plt.plot(epochs,validation_loss,c="blue",label="Validation")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.xticks(epochs)
plt.legend()

epochs1 = range(1, len(accuracy)+1)

fig2 = plt.figure(figsize=(8,4))
plt.plot(epochs1,accuracy,c="red",label="Training")
plt.plot(epochs1,validation_accuracy,c="blue",label="Validation")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.xticks(epochs1)
plt.legend()

# plotGraph(y_test, y_pred, "RF")

"""### **Logistic Regression**"""

from sklearn.linear_model import LogisticRegression
classifier= LogisticRegression(random_state=0)
classifier.fit(x_train, y_train)

y_pred= classifier.predict(x_test)
y_pred

classifier.score(x_test, y_pred)

print(classification_report(y_test, y_pred))

cf_matrix= confusion_matrix(y_test, y_pred)
cf_matrix

import seaborn as sns
sns.heatmap(cf_matrix, annot=True, cbar=False, fmt='g')
cf_matrix

loss = history.history['loss']
validation_loss = history.history['val_loss']
accuracy = history.history['accuracy']
validation_accuracy =history.history['val_accuracy']

epochs = range(1, len(loss)+1)

fig1 = plt.figure(figsize=(8,4))
plt.plot(epochs,loss,c="red",label="Training")
plt.plot(epochs,validation_loss,c="blue",label="Validation")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.xticks(epochs)
plt.legend()

epochs1 = range(1, len(accuracy)+1)

fig2 = plt.figure(figsize=(8,4))
plt.plot(epochs1,accuracy,c="red",label="Training")
plt.plot(epochs1,validation_accuracy,c="blue",label="Validation")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.xticks(epochs1)
plt.legend()

# plotGraph(y_test, y_pred, "LR")

"""### **K Neighbors**"""

from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(x_train, y_train)

y_pred = knn.predict(x_test)
y_pred

knn.score(x_test, y_pred)

print(classification_report(y_test, y_pred))

cf_matrix= confusion_matrix(y_test, y_pred)
cf_matrix

import seaborn as sns
sns.heatmap(cf_matrix, annot=True, cbar=False, fmt='g')
cf_matrix

loss = history.history['loss']
validation_loss = history.history['val_loss']
accuracy = history.history['accuracy']
validation_accuracy =history.history['val_accuracy']

epochs = range(1, len(loss)+1)

fig1 = plt.figure(figsize=(8,4))
plt.plot(epochs,loss,c="red",label="Training")
plt.plot(epochs,validation_loss,c="blue",label="Validation")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.xticks(epochs)
plt.legend()

epochs1 = range(1, len(accuracy)+1)

fig2 = plt.figure(figsize=(8,4))
plt.plot(epochs1,accuracy,c="red",label="Training")
plt.plot(epochs1,validation_accuracy,c="blue",label="Validation")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.xticks(epochs1)
plt.legend()

# plotGraph(y_test, y_pred, "KNN")

"""### **One-Class SVM**"""

from sklearn.datasets import make_classification
from collections import Counter
import matplotlib.pyplot as plt
from sklearn.svm import OneClassSVM
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Create an imbalanced dataset
x, y = make_classification(n_samples=100000, n_features=2, n_informative=2,
                           n_redundant=0, n_repeated=0, n_classes=2,
                           n_clusters_per_class=1,
                           weights=[0.995, 0.005],
                           class_sep=0.5, random_state=0)

# Convert the data from numpy array to a pandas dataframe
df = pd.DataFrame({'feature1': x[:, 0], 'feature2': x[:, 1], 'target': y})

# Check the target distribution
df['target'].value_counts(normalize = True)

# Check the number of records
print('The number of records in the training dataset is', x_train.shape[0])
# print('The number of records in the test dataset is', x_test.shape[0])
print(f"The training dataset has {sorted(Counter(y_train).items())[0][1]} records for the majority class and {sorted(Counter(y_train).items())[1][1]} records for the minority class.")

one_class_svm = OneClassSVM(nu=0.01, kernel = 'rbf', gamma = 'auto').fit(x_train)

# Predict the anomalies
prediction = one_class_svm.predict(x_test)

# Change the anomalies' values to make it consistent with the true values
prediction = [1 if i==-1 else 0 for i in prediction]

# Get the scores for the testing dataset
score = one_class_svm.score_samples(x_test)

# Check the score for 2% of outliers
score_threshold = np.percentile(score, 2)
print(f'The customized score threshold for 2% of outliers is {score_threshold:.2f}')

# Check the model performance at 2% threshold
customized_prediction = [1 if i < score_threshold else 0 for i in score]

# # Check the prediction performance
print(classification_report(y_test, customized_prediction))

cf_matrix= confusion_matrix(y_test, y_pred)
cf_matrix

import seaborn as sns
sns.heatmap(cf_matrix, annot=True, cbar=False, fmt='g')
cf_matrix

loss = history.history['loss']
validation_loss = history.history['val_loss']
accuracy = history.history['accuracy']
validation_accuracy =history.history['val_accuracy']

epochs = range(1, len(loss)+1)

fig1 = plt.figure(figsize=(8,4))
plt.plot(epochs,loss,c="red",label="Training")
plt.plot(epochs,validation_loss,c="blue",label="Validation")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.xticks(epochs)
plt.legend()

epochs1 = range(1, len(accuracy)+1)

fig2 = plt.figure(figsize=(8,4))
plt.plot(epochs1,accuracy,c="red",label="Training")
plt.plot(epochs1,validation_accuracy,c="blue",label="Validation")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.xticks(epochs1)
plt.legend()

# plotGraph(y_test, y_pred, "1CSVM")

type(x_test)

"""### LSTM"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Scale input variables using MinMaxScaler
sc = MinMaxScaler(feature_range=(0,1))
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# Reshape input variables for LSTM model
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

# Build LSTM model
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50))
model.add(Dropout(0.2))
model.add(Dense(units=1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train LSTM model
model.fit(x_train, y_train, epochs=100, batch_size=32)

# Predict test set results
y_pred = model.predict(x_test)
y_pred = (y_pred > 0.5)

# Compute evaluation metrics
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

# Print evaluation metrics
print("Accuracy:", acc)
print("Precision:", prec)
print("Recall:", rec)
print("F1 Score:", f1)
print("Confusion Matrix:", cm)

# # Check the prediction performance
print(classification_report(y_test, y_pred))

import seaborn as sns
sns.heatmap(cf_matrix, annot=True, cbar=False, fmt='g')
cf_matrix

loss = history.history['loss']
validation_loss = history.history['val_loss']
accuracy = history.history['accuracy']
validation_accuracy =history.history['val_accuracy']

epochs = range(1, len(loss)+1)

fig1 = plt.figure(figsize=(8,4))
plt.plot(epochs,loss,c="red",label="Training")
plt.plot(epochs,validation_loss,c="blue",label="Validation")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.xticks(epochs)
plt.legend()

epochs1 = range(1, len(accuracy)+1)

fig2 = plt.figure(figsize=(8,4))
plt.plot(epochs1,accuracy,c="red",label="Training")
plt.plot(epochs1,validation_accuracy,c="blue",label="Validation")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.xticks(epochs1)
plt.legend()

# plotGraph(y_test, y_pred, "LSTM")

"""### **BILSTM**"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout, Bidirectional
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Build the BiLSTM model
model = Sequential()
model.add(Bidirectional(LSTM(64, activation='relu', input_shape=(x_train.shape[1], 1))))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
history = model.fit(x_train.reshape(-1, x_train.shape[1], 1), y_train, epochs=50, batch_size=32, validation_split=0.1)

# Evaluate the model
y_pred = model.predict(x_test.reshape(-1, x_test.shape[1], 1))
y_pred = y_pred > 0.5  # convert probabilities to binary predictions

print('Accuracy:', accuracy_score(y_test, y_pred))
print('Precision:', precision_score(y_test, y_pred))
print('Recall:', recall_score(y_test, y_pred))
print('F1 score:', f1_score(y_test, y_pred))
print('Confusion matrix:', confusion_matrix(y_test, y_pred))

# # Check the prediction performance
print(classification_report(y_test, y_pred))

from sklearn.metrics import confusion_matrix
cf_matrix = confusion_matrix(y_test, y_pred)
cf_matrix

import seaborn as sns
sns.heatmap(cf_matrix, annot=True, cbar=False, fmt='g')
cf_matrix

loss = history.history['loss']
validation_loss = history.history['val_loss']
accuracy = history.history['accuracy']
validation_accuracy =history.history['val_accuracy']

epochs = range(1, len(loss)+1)

fig1 = plt.figure(figsize=(8,4))
plt.plot(epochs,loss,c="red",label="Training")
plt.plot(epochs,validation_loss,c="blue",label="Validation")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.xticks(epochs)
plt.legend()

epochs1 = range(1, len(accuracy)+1)

fig2 = plt.figure(figsize=(8,4))
plt.plot(epochs1,accuracy,c="red",label="Training")
plt.plot(epochs1,validation_accuracy,c="blue",label="Validation")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.xticks(epochs1)
plt.legend()
# plot_bar_chart(y_test, y_pred, "BILSTM")

"""### **Combined Model**"""

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout, Bidirectional
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Scale input variables using MinMaxScaler
sc = MinMaxScaler(feature_range=(0,1))
x_scaled = sc.fit_transform(x)

# Reshape input variables for LSTM model
x_reshaped = np.reshape(x_scaled, (x_scaled.shape[0], x_scaled.shape[1], 1))

# Split the data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(x_reshaped, y, test_size=0.2, random_state=42)

# Build the BiLSTM model
model = Sequential()
model.add(Bidirectional(LSTM(64, activation='relu', input_shape=(x_train.shape[1], 1))))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
history = model.fit(x_train, y_train, epochs=50, batch_size=32, validation_split=0.1)

# Evaluate the model
y_pred = model.predict(x_test)
y_pred = y_pred > 0.5  # convert probabilities to binary predictions

print('Accuracy:', accuracy_score(y_test, y_pred))
print('Precision:', precision_score(y_test, y_pred))
print('Recall:', recall_score(y_test, y_pred))
print('F1 score:', f1_score(y_test, y_pred))
print('Confusion matrix:', confusion_matrix(y_test, y_pred))

# # Check the prediction performance
print(classification_report(y_test, y_pred))

from sklearn.metrics import confusion_matrix
cf_matrix = confusion_matrix(y_test, y_pred)
cf_matrix

import seaborn as sns
sns.heatmap(cf_matrix, annot=True, cbar=False, fmt='g')
cf_matrix

loss = history.history['loss']
validation_loss = history.history['val_loss']
accuracy = history.history['accuracy']
validation_accuracy=history.history['val_accuracy']

epochs = range(1, len(loss)+1)

fig1 = plt.figure(figsize=(8,4))
plt.plot(epochs,loss,c="red",label="Training")
plt.plot(epochs,validation_loss,c="blue",label="Validation")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.xticks(epochs)
plt.legend()

epochs1 = range(1, len(accuracy)+1)

fig2 = plt.figure(figsize=(8,4))
plt.plot(epochs1,accuracy,c="red",label="Training")
plt.plot(epochs1,validation_accuracy,c="blue",label="Validation")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.xticks(epochs1)
plt.legend()

# plotGraph(y_test, y_pred, "Combined")