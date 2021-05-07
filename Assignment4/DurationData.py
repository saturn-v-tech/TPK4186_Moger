import pandas as pd
import csv
import numpy as np
import os

inputFile = 'Project Data'

df1 = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
delay_vector1 = []
delay_vector2 = []

for filename in os.listdir(inputFile):
    f = os.path.join(inputFile, filename)
    # Checking if it is a file
    if os.path.isfile(f):
        with open(f) as csv_file:
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

        # Creating training data

        df1 = pd.read_csv("project001.tsv", sep = '\t', header = 2)

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