# Assignment 4 - TPK4186 - Assignment 4

# Fredrik Moger
# Mats Emil Mossefin 
# Group 1 

# ---------------------------------------# 

# Task 3: Early prediction of actual durations


# 1. Imported packages
# --------------------------------------

import pandas as pd
import csv 
import matplotlib.pyplot as plt
import os 
import numpy as np

# Global variables used when writing the code
# -------------------------------------------

class Parser: 

    def __init__(self):
        self.name = None
        self.expectedDuration = None
        self.dataframe = pd.DataFrame()

    def readFile(self, inputFile):

        # Assign attributes such as name and expected duration 
        
        df = pd.DataFrame() # Setting up empty data frame for specific project 

        df_main = pd.DataFrame() # Setting up empty data frame for all project data

        delay_vector = []

        for filename in os.listdir(inputFile):
            f = os.path.join(inputFile, filename)
            # Checking if it is a file
            if os.path.isfile(f):
                with open(f) as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter = '\t')
                    count = 0  
                    for row in csv_reader:
                        if count == 0: 
                            self.name = row[1]
                        elif count == 1:
                            self.expectedDuration = row[1]
                        else:
                            break
                        count += 1 
                    # print(self.name, self.expectedDuration)

                    # duration = self.expectedDuration

                    # Normalization of data structure using pandas data frame 

                    df = pd.read_csv(f, sep = '\t', header = 2)

                    duration = df['Week'].iloc[-1]

                    df['Week'] = df['Week']/int(self.expectedDuration)
                    df['Foundation'] = df['Foundation']/100 # This is not neseccary, but we prefered to have all the data on same format. 
                    df['Framing'] = df['Framing']/100
                    df['CurtainWall'] = df['CurtainWall']/100
                    df['HVAC'] = df['HVAC']/100
                    df['FireFighting'] = df['FireFighting']/100
                    df['Elevator'] = df['Elevator']/100
                    df['Electrical'] = df['Electrical']/100
                    df['ArchitecturalFinishing'] = df['ArchitecturalFinishing']/100

                    for i in range(len(df)):
                        delay_vector.append(int(duration))
                    
                    # print(delay_vector)

                    df['ActualDuration'] =  delay_vector

                    delay_vector = []

                    # print(df.head())

                    # self.dataframe = df

                # print(df_main)
                
                # delay_vector.append(df['Week'].iloc[-1])

            df_main = pd.concat([df_main, df])
        
        df_main.reset_index(drop=True, inplace=True)
        # print(df_main.head(), df_main.tail())
        return df_main

# Defining class

parser = Parser()

inputFile = 'Project Data'

parser.readFile(inputFile)