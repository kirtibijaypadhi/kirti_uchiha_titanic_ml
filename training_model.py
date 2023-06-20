#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas
import seaborn
import matplotlib.pyplot
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

data_form = pandas.read_csv('train.csv')
del data_form['Cabin']
data_form.loc[data_form['Age'] > 70, 'Age'] = 70
data_form.loc[data_form['Fare']>400, 'Fare'] = data_form['Fare'].median()
data_form['Age'].fillna(data_form['Age'].median(), inplace=True)
data_form['Embarked'].fillna('S', inplace=True)
def get_title(name):
  if '.' in name:
    return name.split(',')[1].split('.')[0].strip()
  else:
    return 'No title in name'
titles = set(x for x in data_form.Name.map(lambda x: get_title(x)))
def short_title(x):
  title = x['Title']
  if title in ['Col', 'Capt', 'Major']:
    return 'Officer'
  elif title in ['Jonkheer', 'Don','the Countess', 'Dona','Lady','Sir']:
    return 'Royalty'
  elif title == 'Mme':
    return 'Mrs'
  elif title in ['Mlle', 'Ms']:
    return 'Miss'
  else:
    return title
data_form['Title'] = data_form['Name'].map(lambda x:get_title(x))
data_form['Title'] = data_form.apply(short_title, axis=1)
data_form.drop('Name', axis=1, inplace=True)
data_form.replace(('male', 'female'), (0,1),inplace=True)
data_form.replace(('S','C','Q'), (0,1,2),inplace=True)
data_form.replace(('Mr','Miss','Mrs','Master','Dr','Rev','Royalty','Officer'), (0,1,2,3,4,5,6,7),inplace=True)

x = data_form.drop(['Survived', 'PassengerId', 'Ticket'], axis=1)
y = data_form['Survived']
# x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.1)


# from sklearn.metrics import accuracy_score
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.1)
randomforest = RandomForestClassifier()
randomforest.fit(x_train, y_train)
y_pred = randomforest.predict(x_val)
# acc_randomforest = round(accuracy_score(y_pred, y_val) * 100, 2)
# print('accuracy : {}'.format(acc_randomforest))
filename = 'titanic_model.sav'
pickle.dump(randomforest, open(filename, 'wb'))


# In[10]:





# In[3]:


def prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title):
    import pickle
    x = [[pclass,sex,age,sibsp,parch,fare,embarked,title]]
    randomforest = pickle.load(open('titanic_model.sav','rb'))
    predictions = randomforest.predict(x)
    print(predictions)


# In[4]:


prediction_model(1,1,11,1,1,19,1,1)


# In[ ]:




