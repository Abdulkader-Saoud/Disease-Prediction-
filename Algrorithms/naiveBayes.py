import pandas as pd
from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
import pickle
import time

dataset= pd.read_csv("processed_data.csv")
X = dataset.iloc[:,1:]
Y = dataset.iloc[:,0]


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)
X_train = X_train.values
X_test = X_test.values
startTime = time.time()
NB = BernoulliNB()

model = NB.fit(X_train, y_train)

training_time = time.time() - startTime

cls_pred = NB.predict(X_test)
acc = accuracy_score(y_test,cls_pred)
precision = precision_score(y_test, cls_pred, average='weighted', zero_division=0)
recall = recall_score(y_test, cls_pred, average='weighted', zero_division=0)

print("Accuracy = " + str(acc))
print("Training time = " + str(training_time))
print('Precision: %.3f' % precision + ' Recall: %.3f' % recall)

with open('./Models/NB_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)
