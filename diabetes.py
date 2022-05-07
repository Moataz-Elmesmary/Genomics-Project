import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('diabetes.csv')
df

df.shape
df.info()
df.describe()

print(df['Outcome'].value_counts())
o = df['Outcome'].value_counts().plot(kind="bar")
# 0 Non-Diabetic
# 1 Diabetic

#Correlation between all the features before cleaning

plt.figure(figsize=(12,10))
# seaborn has an easy method to showcase heatmap
p = sns.heatmap(df.corr(), annot=True,cmap ='RdYlGn')

df.groupby('Outcome').mean()

df.isnull().sum()




df = df.rename(columns={'DiabetesPedigreeFunction': 'DPF'})

df_copy = df.copy(deep=True)
df_copy[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = df_copy[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.NaN)
# Showing the Count of NANs
print(df_copy.isnull().sum())


df_copy['Glucose'].fillna(df_copy['Glucose'].mean(), inplace = True)
df_copy['BloodPressure'].fillna(df_copy['BloodPressure'].mean(), inplace = True)
df_copy['SkinThickness'].fillna(df_copy['SkinThickness'].mean(), inplace = True)
df_copy['Insulin'].fillna(df_copy['Insulin'].median(), inplace = True)
df_copy['BMI'].fillna(df_copy['BMI'].median(), inplace = True)

# separating the data and labels
X = df.drop(columns = 'Outcome', axis=1)
Y = df['Outcome']

print(X.head())

print(Y.head())


from sklearn.model_selection import train_test_split

X = df.drop(columns='Outcome')

y = df['Outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.35)


from sklearn.ensemble import RandomForestClassifier


classifier = RandomForestClassifier(n_estimators=205)
classifier.fit(X_train, y_train)

#Getting the accuracy score for Random Forest
from sklearn.metrics import accuracy_score

# accuracy score on the training data
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, y_train)

print('Accuracy score of the training data : ', training_data_accuracy)


# accuracy score on the test data
X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, y_test)

print('Accuracy score of the test data : ', test_data_accuracy)


classifier.feature_importances_

(pd.Series(classifier.feature_importances_, index=X.columns).plot(kind='barh'))
#Here from the above graph, it is clearly visible that Glucose as a feature is the most important in this dataset.

filename = 'diabetes.pkl'
pickle.dump(classifier, open(filename, 'wb'))