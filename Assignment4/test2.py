import pandas as pd
import plotly.express
import csv 


# Assign attributes such as name and expected duration 
df = pd.DataFrame() # Setting up empty data frame for specific project 
df_main = pd.DataFrame() # Setting up empty data frame for all project data
delay_vector = [] # Setting up empty array for delayed time 

inputFile = 'Project Data'

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

        # Normalization of data structure using pandas data frame 

        df = pd.read_csv(f, sep = '\t', header = 2)

        df['Week'] = df['Week']/int(expectedDuration)
        df['Foundation'] = df['Foundation']/100 # This is not neseccary, but we prefered to have all the data on same format. 
        df['Framing'] = df['Framing']/100
        df['CurtainWall'] = df['CurtainWall']/100
        df['HVAC'] = df['HVAC']/100
        df['FireFighting'] = df['FireFighting']/100
        df['Elevator'] = df['Elevator']/100
        df['Electrical'] = df['Electrical']/100
        df['ArchitecturalFinishing'] = df['ArchitecturalFinishing']/100

        delay_vector = (df['Week'].iloc[-1])

        if delay_vector > 1.4:
            delay_vector = np.ones(len(df))
        else: 
            delay_vector = np.zeros(len(df))
        
        df['Fiasco'] = delay_vector 

        self.dataframe = df

    df_main = pd.concat([df_main, df])

df_main.reset_index(drop=True, inplace=True)
# print(df_main.head(), df_main.tail())
return df_main
