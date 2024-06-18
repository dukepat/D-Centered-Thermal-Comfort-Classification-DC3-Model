#%% Import data to script
import pandas as pd
df = pd.read_csv('ashrae_db2.csv',encoding_errors='ignore')

#%% Filtering for Indian data
df1 = df[df['Country'] == 'India']
len(df1)
columns = ['Season', 'City', 'Cooling startegy_building level','Thermal sensation acceptability','Thermal sensation','Thermal preference',
           'Thermal comfort', 'PMV', 'PPD', 'Clo', 'Met', 'Air temperature (C)',
            'Air velocity (m/s)','Relative humidity (%)']
df1 = df1[columns]