# -*- coding: utf-8 -*-
"""naive_bayes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cIQk8HtkYUwtKY-TI4d6sZqPRb3a2YqC

# Naive Bayes
Naive Bayes is one of the most popular classifcation algorithims and one that runs on the basis of the bayes equation of probability. It is highly efficent for problems with lots of numeral probabilities involved. Which makes it perfect for our dataset of  acute inflammations of the urinary bladder and acute
nephritises.

### Importing the libraries
These are the three go to libraries for most ML.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""### Importing the dataset
I imported the dataset through Pandas dataframe then using iloc assign everything besides the last column as our independent variable(s) or X and the last column as our dependent variable or Y. The name of the dataset has to be updated and it must be in the same folder as your .py file or uploaded on Jupyter Notebooks or Google Collab.

For this specific dataset, we can adjust the y dataframe reading to diagnose one disease ('6: ' or '7: ') or both ('6: '). The while loop on the bottom is only activated to categorize the possibilites of both diseases togehter when we choose to predict them together.
"""

dataset = pd.read_csv('diagnosis2.csv')

X = dataset.iloc[:, :6].values
y = dataset.iloc[:, 6:].values

if len(y[0]) == 2:
  var = 0
  row = 0
  col1 = 0
  col2 = 1
  newcol = []
  
  while var < len(y):
      if y[row, col1] == 0 and y[row, col2] == 0:
          newcol.append(['A'])
          row = row + 1
          var = var + 1
      elif y[row, col1] == 1 and y[row, col2] == 0:
          newcol.append(['B'])
          row = row + 1
          var = var + 1
      elif y[row, col1] == 0 and y[row, col2] == 1:
          newcol.append(['C'])
          row = row + 1
          var = var + 1
      elif y[row, col1] == 1 and y[row, col2] == 1:
          newcol.append(['D'])
          row = row + 1
          var = var + 1

  y = np.array(newcol)

"""### Splitting the dataset into the Training set and Test set
Here I used a normal 80/20 test size and  assigned 'random_state' None.
"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = None)

"""### Feature Scaling
We can feature scale our data to make it easier for our model to train on our data and give us accurate results that aren't shifted by the presence of extreme outliers. It's not necessary, but helpful for getting more accurate results.
"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

"""### Training the Naive Bayes model on the Training set
Simple training the model using a Gaussian NB function which is the most common one.
"""

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

"""### Predicting the Test set results
This uses the X_test to predict our diagnosis  and then compares the prediction and actual result in a concatenated print.
"""

y_pred = classifier.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

"""### Making the Confusion Matrix
The confusion matrix is a useful metric for classification models to allow us to visualize the correct positive, false positive, false negative, and correct negative predictions as well as a ultimate accuracy score on the bottom. 

Our model performs to nearly 90% and 95% accuracy for diagnosing the diseases exclusivly and almost 100% accuracy for diagnosing them togehter.
Normal physician diagnosing accuracy is around 80%.
"""

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)