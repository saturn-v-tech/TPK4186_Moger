# Assignment 4 - TPK4186 - Assignment 4

# Fredrik Moger
# Mats Emil Mossefin 
# Group 1 

# ---------------------------------------# 

# Task 1: Normalization and statistics 


# 1. Imported packages
# --------------------------------------

import pandas as pd
import csv 
import matplotlib.pyplot as plt
import os 

# Global variables used when writing the code
# -------------------------------------------

# df = pd.DataFrame()
# name = None 
# expectedDuration = None

# directory = 'Project Data'

# ---------------------------------------------

class Parser: 

    def __init__(self):
        self.name = None
        self.expectedDuration = None
        self.dataframe = pd.DataFrame()

    def readFile(self, inputFile):

        # Assign attributes such as name and expected duration 
        
        df = pd.DataFrame() # Setting up empty data frame for later

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

                # Normalization of data structure using pandas data frame 

                df = pd.read_csv(f, sep = '\t', header = 2)

                df['Week'] = df['Week']/int(self.expectedDuration)
                df['Foundation'] = df['Foundation']/100 # This is not neseccary, but we prefered to have all the data on same format. 
                df['Framing'] = df['Framing']/100
                df['CurtainWall'] = df['CurtainWall']/100
                df['HVAC'] = df['HVAC']/100
                df['FireFighting'] = df['FireFighting']/100
                df['Elevator'] = df['Elevator']/100
                df['Electrical'] = df['Electrical']/100
                df['ArchitecturalFinishing'] = df['ArchitecturalFinishing']/100

                self.dataframe = df

                delay_vector.append(df['Week'].iloc[-1])

        # Histogram plot 

        plt.style.use('ggplot')
        plt.hist(delay_vector, bins = 10)

        plt.xlabel('Percentage overdue, where 1 is on time (bins = 10)', fontsize=10)
        plt.ylabel('# of projects', fontsize=10)
        plt.title('Duration of construction projects')

        plt.show()

# Defining class

parser = Parser()

inputFile = 'Project Data'

parser.readFile(inputFile)