from pandas.core.frame import DataFrame
from scipy.spatial.distance import minkowski
from task2 import *
from sklearn.neighbors import NearestCentroid
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import SGDClassifier
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.model_selection import validation_curve
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt
import random
import warnings
warnings.filterwarnings("ignore")


class Fiasco():
  def __init__(self, inputFile):

    self.X, self.y = self.createXY(inputFile)

  def createXY(self, inputFile):

    df = parser.readFile(inputFile)

    X = df[["Week", "Foundation", "Framing", "CurtainWall", "HVAC"]] # Independent variables, ["FireFighting", "Elevator", "Electrical", "ArchitecturalFinishing"] Rest of params could be added 
    y = df['Fiasco'] # Dependet variables

    X = DataFrame.to_numpy(X) # Had to convert to numpy arrays for the models to fetch data. 
    y = DataFrame.to_numpy(y)

    return X, y

  def createTrainTestSplit(self):

    X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, random_state=32) # Uses random state to control the shuffling. Creates reproducible output across multiple function calls
    
    return X_train, X_test, y_train, y_test

  # Count correct function

  def count_correct(self, model):

    corr, wrong = 0, 0

    for i in range(len(self.y_test)):
      rand_index = random.randint(0, self.X_test.shape[0]-1)
      test = model.predict([self.X_test[rand_index]])

      if test == self.y_test[rand_index]:
        corr += 1

      else:
        wrong += 1

    return corr, wrong


  # Generate a plot of the test and training learning curve

  def plot_learning_curve(self, estimator, title, X, y, ylim=None, cv=None, n_jobs=1, train_sizes=np.linspace(.1, 1.0, 25)):

      plt.figure()
      plt.title(title)

      if ylim is not None:
          plt.ylim(*ylim)

      plt.xlabel("Training examples")
      plt.ylabel("Score")

      train_sizes, train_scores, test_scores = learning_curve(estimator, self.X, self.y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)
      train_scores_mean = np.mean(train_scores, axis=1)
      train_scores_std = np.std(train_scores, axis=1)
      test_scores_mean = np.mean(test_scores, axis=1)
      test_scores_std = np.std(test_scores, axis=1)

      plt.grid()
      plt.fill_between(train_sizes, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std, alpha=0.1, color="r")
      plt.fill_between(train_sizes, test_scores_mean - test_scores_std, test_scores_mean + test_scores_std, alpha=0.1, color="g")
      plt.plot(train_sizes, train_scores_mean, 'o-', color="r", label="Training score")
      plt.plot(train_sizes, test_scores_mean, 'o-', color="g", label="Cross-validation score")
      plt.legend(loc="best")
      
      return plt


# Testing (15 min to run test due to SVC model, comment out SVC/clf3 to make it run faster)

# Initilizing 

inputFile = 'Project Data' # As we use test-train-split we can use all the data

parser = Parser()

fiasco = Fiasco(inputFile)

X, y = fiasco.createXY(inputFile)

X_train, X_test, y_train, y_test = fiasco.createTrainTestSplit()

# Defining classification methods 

clf1 = NearestCentroid(metric = 'manhattan', shrink_threshold=500) # Performs better with the manhattan metric and a high shrink threshold. Remove params to see result with default params. 
clf1.fit(X_train, y_train)

clf2 = SGDClassifier(loss="modified_huber", penalty="l1", max_iter=10000) # Modified huber has a higher tolerance to outliers than default. Penalty l1, adds a penalty equal the abosolute value. 
clf2.fit(X_train, y_train)

clf3 = svm.SVC()
clf3.fit(X_train, y_train)

clf4 = svm.LinearSVC()
clf4.fit(X_train, y_train)

clf5 = KNeighborsClassifier()
clf5.fit(X_train, y_train)

# Plotting results 

plt = fiasco.plot_learning_curve(clf1, "Nearest Centroid, metric = manhattan, shrink threshold = 500", X, y)
plt = fiasco.plot_learning_curve(clf2, "SGD Classifier", X, y)
plt = fiasco.plot_learning_curve(clf3, "SVC", X, y)
plt = fiasco.plot_learning_curve(clf4, "Linear SVC", X, y)
plt = fiasco.plot_learning_curve(clf5, "K NeighborsClassifier", X, y)
plt.show()











# EXTRA _________________________________________________

  # This function could be used for testing - but after cleaning the code structure, it was no longer neccessary. 
  # def fiascoML(self, inputFile):

  #   clf1 = NearestCentroid(metric = 'manhattan', shrink_threshold=500) # Performs better with the manhattan metric and a high shrink threshold. Remove params to see result with default params. 
  #   clf1.fit(self.X_train, self.y_train)

  #   clf2 = SGDClassifier(loss="modified_huber", penalty="l1", max_iter=10000) # Modified huber has a higher tolerance to outliers than default. Penalty l1, adds a penalty equal the abosolute value. 
  #   clf2.fit(self.X_train, self.y_train)

  #   clf3 = svm.SVC()
  #   clf3.fit(self.X_train, self.y_train)

  #   clf4 = svm.LinearSVC()
  #   clf4.fit(self.X_train, self.y_train)

  #   clf5 = KNeighborsClassifier()
  #   clf5.fit(self.X_train, self.y_train)

  #   pred1 = clf1.predict(self.X_test)
  #   pred2 = clf2.predict(self.X_test)
  #   pred3 = clf3.predict(self.X_test)
  #   pred4 = clf4.predict(self.X_test)
  #   pred5 = clf5.predict(self.X_test)

  #   return clf1, clf2, clf3, clf4, clf5