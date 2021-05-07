import pandas as pd
import csv 
import matplotlib.pyplot as plt
import os 
import numpy

directory = 'Project Data'

df = pd.DataFrame()

Foundation = 0 
Framing = 0 
CurtainWall = 0 
HVAC = 0 
FireFighting = 0 
Elevator = 0 
Electrical = 0 
ArchitecturalFinishing = 0 
Weeks = 0 

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # Checking if it is a file
    if os.path.isfile(f):
        df = pd.read_csv(f, sep = '\t', header = 2)
        Foundation += 1 
        Framing += 1
        CurtainWall += 1 
        HVAC += 1
        FireFighting += 1 
        Elevator += 1
        Electrical += 1 
        ArchitecturalFinishing += 1 
        Weeks += len(df)
    for i in df.Foundation:
        if 0 < i < 100:
            Foundation += 1 
    for i in df.Framing:
        if 0 < i < 100:
            Framing += 1 
    for i in df.CurtainWall:
        if 0 < i < 100:
            CurtainWall += 1 
    for i in df.HVAC:
        if 0 < i < 100:
            HVAC += 1 
    for i in df.FireFighting:
        if 0 < i < 100:
            FireFighting += 1
    for i in df.Elevator:
        if 0 < i < 100:
            Elevator += 1 
    for i in df.Electrical:
        if 0 < i < 100:
            Electrical += 1 
    for i in df.ArchitecturalFinishing:
        if 0 < i < 100:
            ArchitecturalFinishing += 1
    
# print(Foundation/Weeks, Framing/Weeks, CurtainWall/Weeks, HVAC/Weeks, FireFighting/Weeks, Elevator/Weeks, Electrical/Weeks, ArchitecturalFinishing/Weeks)

# labels = ['Foundation', 'Framing', 'CurtainWall', 'FireFighting', 'Elevator', 'Electrical', 'ArchitecturalFinishing']

lables = ['Average time spent by work area']
a = Foundation/Weeks
b = Framing/Weeks
c = CurtainWall/Weeks
d = FireFighting/Weeks
e = Elevator/Weeks
f = Electrical/Weeks
g = ArchitecturalFinishing/Weeks

print(a, b, c, d, e, f, g)

# fig, ax = plt.subplots()
# ax.bar(lables, a, width = 0.35, label = 'Foundation')
# ax.bar(lables, b, width = 0.35, bottom = a, label = 'Framing')
# ax.bar(lables, c, width = 0.35, bottom = b, label = 'CurtainWall')
# ax.bar(lables, d, width = 0.35, bottom = c, label = 'FireFighting')
# ax.bar(lables, e, width = 0.35, bottom = d, label = 'Elevator')
# ax.bar(lables, f, width = 0.35, bottom = e, label = 'Electrical')
# ax.bar(lables, g, width = 0.35, bottom = f, label = 'ArchitecturalFinishing')


# ax.legend()
# plt.show()

df = pd.read_csv("project001.tsv", sep = '\t', header = 2)

for i in df.Foundation:
    if 0 < i < 100:
        Foundation += 1 

print(Foundation)

print(df.tail(5))
print(len(df))

df.plot(x = 'Week', y = ['Foundation', 'Framing', 'CurtainWall', 'HVAC', 'FireFighting', 'Elevator', 'Electrical', 'ArchitecturalFinishing'], kind = 'line')
plt.show()