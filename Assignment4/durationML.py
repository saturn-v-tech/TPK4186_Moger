from task3 import *
from sklearn import linear_model
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor


parser = Parser()

inputFile = 'PD_Duration_Train'

df = parser.readFile(inputFile)

X = df[["Week", "Foundation", "Framing", "CurtainWall", "HVAC", "FireFighting", "Elevator", "Electrical", "ArchitecturalFinishing"]]
y = df['ActualDuration']

# print(X)

regr_linear = linear_model.LinearRegression()
regr_linear.fit(X, y)

regr_lasso = linear_model.Lasso(alpha = 0.001)
regr_lasso.fit(X, y)

regr_lars = linear_model.Lars(n_nonzero_coefs=500)
regr_lars.fit(X, y)

regressor = DecisionTreeRegressor(random_state=0)
# cross_val_score(regressor, X, y, cv=10)
regressor.fit(X, y)


# [0.027322, 0.862, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] day nr: 5
# [1.473684, 1.000, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.967] day nr: ?
# [0.7049180327868853,1.0,1.0,0.0,0.35200000000000004,0.35700000000000004,1.0,0.6970000000000001,0.0] Day nr: 128
# [1.174863387978142, 1.0, 1.0, 0.38, 1.0, 1.0, 1.0, 1.0, 0.052000000000000005] day nr: 214

inputFile = 'PD_Fiasco_Test'

df2 = parser.readFile(inputFile)

# print(df2.iloc[2])

for i in range(25, len(df2)-25, 10):
    week = df2["Week"].iloc[i]
    foundation = df2["Foundation"].iloc[i]
    framing = df2["Framing"].iloc[i]
    curtainWall = df2["CurtainWall"].iloc[i]
    HVAC = df2["HVAC"].iloc[i]
    fireFighting = df2["FireFighting"].iloc[i]
    elevator = df2["Elevator"].iloc[i]
    electrical = df2["Electrical"].iloc[i]
    architecturalFinishing = df2["ArchitecturalFinishing"].iloc[i]

    pred = regr_linear.predict([[week, foundation, framing, curtainWall, HVAC, fireFighting, elevator, electrical, architecturalFinishing]])
    pred2 = regr_lasso.predict([[week, foundation, framing, curtainWall, HVAC, fireFighting, elevator, electrical, architecturalFinishing]])
    pred3 = regr_lars.predict([[week, foundation, framing, curtainWall, HVAC, fireFighting, elevator, electrical, architecturalFinishing]])
    pred4 = regressor.predict([[week, foundation, framing, curtainWall, HVAC, fireFighting, elevator, electrical, architecturalFinishing]])

    print(pred, pred2, pred3, pred4)

# pred4 = regressor.predict([[1.473684, 1.000, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.967]])

# print(pred4)

    # [week, foundation, framing, curtainWall, HVAC, fireFighting, elevator, electrical, architecturalFinishing]

    # print([week, foundation, framing, curtainWall, HVAC, fireFighting, elevator, electrical, architecturalFinishing])

    # predictedDuration = regr.predict([df2["Week"].iloc[i], df2["Foundation"].iloc[i], df2["Framing"].iloc[i], df2["CurtainWall"].iloc[i], df2["HVAC"].iloc[i], df2["FireFighting"].iloc[i], df2["Elevator"].iloc[i], df2["Electrical"].iloc[i], df2["ArchitecturalFinishing"].iloc[i]])
    # print([df2["Week"].iloc[i], df2["Foundation"].iloc[i], df2["Framing"].iloc[i], df2["CurtainWall"].iloc[i], df2["HVAC"].iloc[i], df2["FireFighting"].iloc[i], df2["Elevator"].iloc[i], df2["Electrical"].iloc[i], df2["ArchitecturalFinishing"].iloc[i]])

# predictedDuration = regr.predict([[1.4894736842105263, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.9]])

# print(predictedDuration)