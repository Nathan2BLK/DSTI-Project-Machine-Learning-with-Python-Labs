import pandas as pd
import glob
import os
import subprocess



folder_path = r"C:\Users\natha\OneDrive\Documents\CIV-SurfaceProNDB\SCHOOL\DSTI\Cours\Python Labs\-DSTI-Project-Machine-Learning-with-Python-Labs\DataBase\Extract_ML_DB"
csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

# Iterate through every file in the folder
for csv_file in csv_files:
    # Read the CSV file using pandas
    df = pd.read_csv(csv_file)
    print(str(csv_file).split('\\')[-1])
    cor = df.corr()
    print(cor['average_rating'])
    

    