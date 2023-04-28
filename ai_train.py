
import pickle
import pandas as pd
import numpy as np

from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier


PATH = './data_ai/Crop_recommendation.csv'
df = pd.read_csv(PATH)
df.shape

df.columns

features = df[['N', 'P','K','temperature', 'humidity', 'ph', 'rainfall']]
target = df['label']
labels = df['label']

Xtrain, Xtest, Ytrain, Ytest = train_test_split(features,target,test_size = 0.2,random_state =2)

# Initializing empty lists to append all model's name and corresponding name
acc = []
model = []

LogReg = LogisticRegression(random_state=2, max_iter=500)

LogReg.fit(Xtrain,Ytrain)

predicted_values = LogReg.predict(Xtest)

x = metrics.accuracy_score(Ytest, predicted_values)
acc.append(x)
model.append('Logistic Regression')
print("Logistic Regression's Accuracy is: ", x)

print(classification_report(Ytest,predicted_values))

# Save Trained Model to use for prediction
LR_pkl_filename = './data_ai/LogisticRegression.pkl'
# Open the file to save as pkl file
LR_Model_pkl = open(LR_pkl_filename, 'wb')
pickle.dump(LogReg, LR_Model_pkl)
# Close the pickle instances
LR_Model_pkl.close()





# Make a prediction
# data_ai sequence: N, P, K, Temp, Moisture, pH, Rainfall (mm)
data = np.array([[32, 12, 30, 25, 98, 5.0, 218]])


prediction = LogReg.predict(data)
print(prediction)