import pandas as pd
import numpy as np
import pickle


df = pd.read_csv('diabetes.csv')
df

df = df.rename(columns={'DiabetesPedigreeFunction': 'DPF'})

df_copy = df.copy(deep=True)
df_copy[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = df_copy[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.NaN)
df_copy['Glucose'].fillna(df_copy['Glucose'].mean(), inplace = True)
df_copy['BloodPressure'].fillna(df_copy['BloodPressure'].mean(), inplace = True)
df_copy['SkinThickness'].fillna(df_copy['SkinThickness'].mean(), inplace = True)
df_copy['Insulin'].fillna(df_copy['Insulin'].median(), inplace = True)
df_copy['BMI'].fillna(df_copy['BMI'].median(), inplace = True)


from sklearn.model_selection import train_test_split

X = df.drop(columns='Outcome')

y = df['Outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)


from sklearn.ensemble import RandomForestClassifier


classifier = RandomForestClassifier(n_estimators=20)
classifier.fit(X_train, y_train)

filename = 'diabetes.pkl'
pickle.dump(classifier, open(filename, 'wb'))