from pathlib import Path
from importlib import resources
import pandas as pd
import matplotlib.pyplot as plt

def activity1():
# This script is located in the project root, so find the path to the current file and then go to the parent of that file
    project_root = Path(__file__).parent.parent

# Find the .csv file relative to the project root and join to that path the data folder and then the example.csv file
    csv_file = project_root.joinpath('data', 'paralympics_raw.csv')
# csv_file = project_root / 'data' / 'example.csv' # this notation would also work, even though you think the '/' is only unix/macOS

# Check if the file exists, this will print 'true' if it exists
    print(csv_file.exists())
    return csv_file

def activity2():
    csv_file = activity1()
    df = pd.read_csv(csv_file)
    print(df.describe())
    return df

def activity3():
    df = activity2()
    missing_rows = df[df.isna().any(axis=1)]
    print(missing_rows)
    

def activity4():
    df = activity2()
    df.plot()
    plt.show()

def activity5():
    df = activity2()
    print(df['type'].unique(),'\n')
    print(df['type'].value_counts())

activity5()