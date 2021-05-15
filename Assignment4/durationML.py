from task3 import *
from sklearn import linear_model
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.model_selection import validation_curve
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt
import random
import warnings
warnings.filterwarnings("ignore")

parser = Parser()

# inputFile = 'PD_Duration_Train'

inputFile = 'Project Data'

df = parser.readFile(inputFile)

X = df[["Week", "Foundation", "Framing", "CurtainWall", "HVAC", "FireFighting", "Elevator", "Electrical", "ArchitecturalFinishing"]] # Independent variables 
y = df['ActualDuration'] # Dependent variable 

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=32)

print(len(X_train), len(y_train))

regr_linear = linear_model.LinearRegression()
regr_linear.fit(X, y)

regr_lasso = linear_model.Lasso(alpha = 0.001)
regr_lasso.fit(X, y)

regr_lars = linear_model.Lars(n_nonzero_coefs=500)
regr_lars.fit(X, y)

regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X, y)

inputFile = 'PD_Fiasco_Test'

df2 = parser.readFile(inputFile)

# for i in range(25, len(df2)-25, 10):
#     week = df2["Week"].iloc[i]
#     foundation = df2["Foundation"].iloc[i]
#     framing = df2["Framing"].iloc[i]
#     curtainWall = df2["CurtainWall"].iloc[i]
#     HVAC = df2["HVAC"].iloc[i]
#     fireFighting = df2["FireFighting"].iloc[i]
#     elevator = df2["Elevator"].iloc[i]
#     electrical = df2["Electrical"].iloc[i]
#     architecturalFinishing = df2["ArchitecturalFinishing"].iloc[i]

#     pred = regr_linear.predict([[week, foundation, framing, curtainWall, HVAC, fireFighting, elevator, electrical, architecturalFinishing]])
#     pred2 = regr_lasso.predict([[week, foundation, framing, curtainWall, HVAC, fireFighting, elevator, electrical, architecturalFinishing]])
#     pred3 = regr_lars.predict([[week, foundation, framing, curtainWall, HVAC, fireFighting, elevator, electrical, architecturalFinishing]])
#     pred4 = regressor.predict([[week, foundation, framing, curtainWall, HVAC, fireFighting, elevator, electrical, architecturalFinishing]])

#     print(pred, pred2, pred3, pred4)

def plot(model):
    # plt.scatter(X_train, y_train, color = "red")
    plt.plot(X_train, model.predict(X_train), color = "green")
    plt.title("(Training set)")
    plt.xlabel("Delay")
    plt.ylabel("Duration")
    plt.show()

    plt.scatter(X_test, y_test, color = "red")
    plt.plot(X_train, model.predict(X_train), color = "green")
    plt.title("Salary vs Experience (Testing set)")
    plt.xlabel("Years of Experience")
    plt.ylabel("Salary")
    plt.show()

plot(regr_linear)