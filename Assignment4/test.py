import pandas as pd
import csv
import numpy as np

df1 = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
delay_vector1 = []
delay_vector2 = []

with open("project001.tsv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = '\t')
    count = 0  
    for row in csv_reader:
        if count == 0: 
            name = row[1]
        elif count == 1:
            expectedDuration = row[1]
        else:
            break
        count += 1 

# Project 1

df1 = pd.read_csv("project076.tsv", sep = '\t', header = 2)

duration1 = df1['Week'].iloc[-1]

df1['Week'] = df1['Week']/int(expectedDuration)
df1['Foundation'] = df1['Foundation']/100 # This is not neseccary, but we prefered to have all the data on same format. 
df1['Framing'] = df1['Framing']/100
df1['CurtainWall'] = df1['CurtainWall']/100
df1['HVAC'] = df1['HVAC']/100
df1['FireFighting'] = df1['FireFighting']/100
df1['Elevator'] = df1['Elevator']/100
df1['Electrical'] = df1['Electrical']/100
df1['ArchitecturalFinishing'] = df1['ArchitecturalFinishing']/100

for i in range(len(df1)):
    delay_vector1.append(int(duration1))

df1['ActualDuration'] = delay_vector1

df1.to_csv('Project76')

# print(df1)

# Project 2

# df2 = pd.read_csv("project002.tsv", sep = '\t', header = 2)

# duration2 = df2['Week'].iloc[-1]

# df2['Week'] = df2['Week']/int(expectedDuration)
# df2['Foundation'] = df2['Foundation']/100 # This is not neseccary, but we prefered to have all the data on same format. 
# df2['Framing'] = df2['Framing']/100
# df2['CurtainWall'] = df2['CurtainWall']/100
# df2['HVAC'] = df2['HVAC']/100
# df2['FireFighting'] = df2['FireFighting']/100
# df2['Elevator'] = df2['Elevator']/100
# df2['Electrical'] = df2['Electrical']/100
# df2['ArchitecturalFinishing'] = df2['ArchitecturalFinishing']/100

# for i in range(len(df2)):
#     delay_vector2.append(int(duration2))

# df2['ActualDuration'] = delay_vector2

# print(df2)

# Append into df3

# df3 = pd.concat([df1, df2])
# df3.reset_index(drop=True, inplace=True)

# print(df3)