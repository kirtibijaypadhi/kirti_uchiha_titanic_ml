#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas


# In[3]:


import seaborn


# In[4]:


import matplotlib.pyplot


# In[5]:


data = pandas.read_csv('train.csv')


# In[6]:


pandas.crosstab(data['Sex'], data['Survived'])


# In[7]:


data.columns


# In[8]:


pandas.crosstab(data['Age'], data['Survived'])


# In[9]:


pandas.crosstab(data['Pclass'], data['Survived'])


# In[10]:


pandas.crosstab(data['Pclass'], data['Sex'])


# In[11]:


data_form = pandas.read_csv('train.csv')
ax = seaborn.countplot(x='Sex', hue='Survived', palette='Set1', data=data_form)
ax.set(title='Survivors according to sex', xlabel = 'Sex', ylabel = 'Total')
matplotlib.pyplot.show()


# In[12]:


seaborn.catplot(x='Pclass', y='Age', hue='Survived', data=data_form)


# In[13]:


data_form.head()


# In[14]:


graph = seaborn.FacetGrid(data_form, col='Survived')
graph.map(matplotlib.pyplot.hist, 'Fare', bins=20)


# In[15]:


data_form.loc[data_form['Fare'] > 400, 'Fare'] = data_form['Fare'].median()


# In[16]:


graph = seaborn.FacetGrid(data_form, col='Survived')
graph.map(matplotlib.pyplot.hist, 'Fare', bins=20)


# In[17]:


graph = seaborn.FacetGrid(data_form, col='Survived')
graph.map(matplotlib.pyplot.hist, 'Age', bins=20)


# In[18]:


data_form.loc[data_form['Age'] > 70, 'Age'] = 70


# In[19]:


graph = seaborn.FacetGrid(data_form, col='Survived')
graph.map(matplotlib.pyplot.hist, 'Age', bins=20)


# In[13]:


import pandas


# In[14]:


data_form = pandas.read_csv('train.csv')


# In[15]:


data_form.info()


# In[16]:


for column in data_form:
    print(column, ':', data_form[column].isnull().sum())


# In[ ]:





# In[17]:


data_form['Age'].fillna(data_form['Age'].median(), inplace=True)


# In[18]:


for i in data_form:
    print(i,':', data_form[i].isnull().sum())


# In[19]:


print(data_form['Embarked'].value_counts())


# In[20]:


data_form['Embarked'].fillna('S', inplace=True)


# In[21]:


for i in data_form:
    print(i, ':', data_form[i].isnull().sum())


# In[22]:


del data_form['Cabin']


# In[23]:


for i in data_form:
    print(i,':', data_form[i].isnull().sum())


# In[32]:


import pandas
data_frame = pandas.read_csv('Train.csv')
for i in range(20):
    print(data_form['Name'][i])


# In[33]:


def get_title(name):
    if '.' in name:
        return name.split(',')[1].split('.')[0].strip()
    else:
        return 'No title in name'


# In[34]:


titles = set([x for x in data_form.Name.map(lambda x: get_title(x))])


# In[35]:


print(titles)


# In[36]:


def shorter_titles(x):
    title = x['Title']
    if title in ['Capt', 'Col', 'Major']:
        return 'Officer'
    elif title in ['Jonkheer','Don','the Countess','Dona','Lady','Sir']:
        return 'Royalty'
    elif title == 'Mme':
        return 'Mrs'
    elif title in ['Mlle', 'Ms']:
        return 'Miss'
    else:
        return title


# In[42]:


data_form['Title'] = data_form['Name'].map(lambda x: get_title(x))


# In[43]:


data_form['Title'] = data_form.apply(shorter_titles, axis = 1)


# In[44]:


print(data_form.Title.value_counts())


# In[49]:


data_form.drop('Name', axis = 1, inplace=True)


# In[50]:


data_form


# In[51]:


data_form.drop('Ticket', axis=1, inplace=True)


# In[53]:


data_form.sample()


# In[54]:


data_form.Title.value_counts()


# In[55]:


data_form.Sex.value_counts()


# In[59]:


data_form.replace(('male', 'female'), (0,1),inplace=True)


# In[60]:


data_form.Embarked.value_counts()


# In[61]:


data_form.replace(('S','C','Q'),(0,1,2), inplace=True)


# In[62]:


data_form


# In[63]:


data_form.Title.value_counts()


# In[65]:


data_form.replace(('Mr','Miss','Mrs','Master','Dr','Rev','Royalty','Officer'),(0,1,2,3,4,5,6,7), inplace=True)


# In[66]:


data_form.sample()


# In[ ]:




