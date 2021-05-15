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

parser = Parser()

# inputFile = 'PD_Fiasco_Train'
inputFile = 'Project Data'

df = parser.readFile(inputFile)

X = df[["Week", "Foundation", "Framing", "CurtainWall", "HVAC"]] # Independent variables, ["FireFighting", "Elevator", "Electrical", "ArchitecturalFinishing"] should be added for METHOD 1. 
y = df['Fiasco'] # Dependet variables
X = DataFrame.to_numpy(X) 
y = DataFrame.to_numpy(y)
# print(y)
# print(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=32) # this should be commented out if you want to run METHOD 1. 

# print(X_test)

inputFile = 'PD_Fiasco_Test'

df2 = parser.readFile(inputFile)

# clf1 = NearestCentroid()
# clf1.fit(X, y)

# clf2 = SGDClassifier(loss="modified_huber", penalty="l1", max_iter=100)
# clf2.fit(X, y)

# clf3 = svm.SVC()
# clf3.fit(X, y)

# clf4 = svm.LinearSVC()
# clf4.fit(X, y)

clf1 = NearestCentroid(metric = 'manhattan', shrink_threshold=500)
clf1.fit(X_train, y_train)

# clf1 = KNeighborsClassifier()
# clf1.fit(X_train, y_train)

# clf2 = SGDClassifier(loss="modified_huber", penalty="l1", max_iter=100)
# clf2.fit(X_train, y_train)

# clf3 = svm.SVC()
# clf3.fit(X_train, y_train)

# clf4 = svm.LinearSVC()
# clf4.fit(X_train, y_train)


# METHOD 1: Loop through all (or a given range, step, etc.) weeks of a project and predict for each week. The model could therefore be trained on the entire data set, 
# and you will see when the classification models starts prediciting when a project is a fiasco. The limitation of this method is that you will only be able to predict on one 
# dataset at the time. In the model below we have predicted for project 76 as we know that is a fiasco project. With some variation the models starts prediciting fiasco in from 
# week 0.4/1 and outwards.  

# for i in range(20, len(df2)-100, 10):
#     week = df2["Week"].iloc[i]
#     foundation = df2["Foundation"].iloc[i]
#     framing = df2["Framing"].iloc[i]
#     curtainWall = df2["CurtainWall"].iloc[i]
#     HVAC = df2["HVAC"].iloc[i]
#     fireFighting = df2["FireFighting"].iloc[i]
#     elevator = df2["Elevator"].iloc[i]
#     electrical = df2["Electrical"].iloc[i]
#     architecturalFinishing = df2["ArchitecturalFinishing"].iloc[i]

    # pred1 = clf1.predict([[week, foundation, framing, curtainWall, HVAC, fireFighting, elevator, electrical, architecturalFinishing]])
    # pred2 = clf2.predict([[week, foundation, framing, curtainWall, HVAC, fireFighting, elevator, electrical, architecturalFinishing]])
    # pred3 = clf3.predict([[week, foundation, framing, curtainWall, HVAC, fireFighting, elevator, electrical, architecturalFinishing]])
    # pred4 = clf4.predict([[week, foundation, framing, curtainWall, HVAC, fireFighting, elevator, electrical, architecturalFinishing]])

# METHOD 2: Use the train split test function. In order to predict early, we only include the first four activies, e.g., foundation, framing, curtainWall and HVAC. 

pred1 = clf1.predict(X_test)
# pred2 = clf2.predict(X_test)
# pred3 = clf3.predict(X_test)
# pred4 = clf4.predict(X_test)

# print(y_test)

def count_correct(model):
  corr, wrong = 0, 0
  for i in range(len(y_test)):
    rand_index = random.randint(0, X_test.shape[0]-1)
    test = model.predict([X_test[rand_index]])
    if test == y_test[rand_index]:
      corr += 1
    else:
      wrong += 1
  return corr, wrong

# print(count_correct(clf1))

def plot_learning_curve(estimator, title, X, y, ylim=None, cv=None, n_jobs=1, train_sizes=np.linspace(.1, 1.0, 25)):
    """
    Generate a simple plot of the test and traning learning curve.
 
    Parameters
    ----------
    estimator : object type that implements the "fit" and "predict" methods
        An object of that type which is cloned for each validation.
 
    title : string
        Title for the chart.
 
    X : array-like, shape (n_samples, n_features)
        Training vector, where n_samples is the number of samples and
        n_features is the number of features.
 
    y : array-like, shape (n_samples) or (n_samples, n_features), optional
        Target relative to X for classification or regression;
        None for unsupervised learning.
 
    ylim : tuple, shape (ymin, ymax), optional
        Defines minimum and maximum yvalues plotted.
 
    cv : integer, cross-validation generator, optional
        If an integer is passed, it is the number of folds (defaults to 3).
        Specific cross-validation objects can be passed, see
        sklearn.cross_validation module for the list of possible objects
 
    n_jobs : integer, optional
        Number of jobs to run in parallel (default 1).
    """
    plt.figure()
    plt.title(title)
    if ylim is not None:
        plt.ylim(*ylim)
    plt.xlabel("Training examples")
    plt.ylabel("Score")
    train_sizes, train_scores, test_scores = learning_curve(estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)
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

plt = plot_learning_curve(clf1, "Nearest Centroid, metric = manhattan, shrink threshold = 500", X, y)
#plt = plot_learning_curve(clf2, "SGD Classifier", X, y)
# plt = plot_learning_curve(clf3, "SVC", X, y)
# plt = plot_learning_curve(clf4, "Linear SVC", X, y)
plt.show()