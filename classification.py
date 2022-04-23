import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder           
from collections import Counter
from imblearn.over_sampling import SMOTE
from sklearn import metrics
df = pd.read_csv("online_shoppers_intention.csv")
LE = LabelEncoder()
df=df.apply(LE.fit_transform) 
x = df[['Weekend', 'VisitorType']]
y = df['Revenue']

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.3, random_state=124)
print(xtrain.shape, xtest.shape, ytrain.shape, ytest.shape)

#Upsampling through smote
counter = Counter(ytrain)

print("=============================")

for k,v in counter.items():
    per = 100*v/len(ytrain)
    print(f"Class= {k}, n={v} ({per:.2f}%)")

oversample = SMOTE()
xtrain, ytrain = oversample.fit_resample(xtrain, ytrain)

counter = Counter(ytrain)

print("=============================")

for k,v in counter.items():
    per = 100*v/len(ytrain)
    print(f"Class= {k}, n={v} ({per:.2f}%)")

print("=============================")

print("Upsampled data shape: ", xtrain.shape, ytrain.shape)

# instantiate the model (using the default parameters)
propensity_model = LogisticRegression()
# fit the model with data
propensity_model.fit(xtrain,ytrain)
#predict for test dataset
ypred=propensity_model.predict(xtest)
#evaluate the model fit
metrics.accuracy_score(ytest, ypred)

#save the pickle file to be loaded in the streamlit app
import pickle
with open("propensity_model.pkl", 'wb') as pfile:
    pickle.dump(propensity_model, pfile)
