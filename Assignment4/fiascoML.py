from task2 import *
from sklearn.neighbors import NearestCentroid
from sklearn.linear_model import SGDClassifier
from sklearn import svm


parser = Parser()

inputFile = 'PD_Fiasco_Train'

df = parser.readFile(inputFile)

X = df[["Week", "Foundation", "Framing", "CurtainWall", "HVAC", "FireFighting", "Elevator", "Electrical", "ArchitecturalFinishing"]]
y = df['Fiasco']

inputFile = 'PD_Fiasco_Test'

df2 = parser.readFile(inputFile)

clf1 = NearestCentroid()
clf1.fit(X, y)

clf2 = SGDClassifier(loss="modified_huber", penalty="l1", max_iter=100)
clf2.fit(X, y)

clf3 = svm.SVC()
clf3.fit(X, y)

clf4 = svm.LinearSVC()
clf4.fit(X, y)


for i in range(20, len(df2)-100, 10):
    week = df2["Week"].iloc[i]
    foundation = df2["Foundation"].iloc[i]
    framing = df2["Framing"].iloc[i]
    curtainWall = df2["CurtainWall"].iloc[i]
    HVAC = df2["HVAC"].iloc[i]
    fireFighting = df2["FireFighting"].iloc[i]
    elevator = df2["Elevator"].iloc[i]
    electrical = df2["Electrical"].iloc[i]
    architecturalFinishing = df2["ArchitecturalFinishing"].iloc[i]

    pred1 = clf1.predict([[week, foundation, framing, curtainWall, HVAC, fireFighting, elevator, electrical, architecturalFinishing]])
    pred2 = clf2.predict([[week, foundation, framing, curtainWall, HVAC, fireFighting, elevator, electrical, architecturalFinishing]])
    pred3 = clf3.predict([[week, foundation, framing, curtainWall, HVAC, fireFighting, elevator, electrical, architecturalFinishing]])
    pred4 = clf4.predict([[week, foundation, framing, curtainWall, HVAC, fireFighting, elevator, electrical, architecturalFinishing]])

    print(pred1, pred2, pred3, pred4)