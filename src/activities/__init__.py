from pathlib import Path
from importlib import resources
import pandas as pd

def activity1():
# This script is located in the project root, so find the path to the current file and then go to the parent of that file
    project_root = Path(__file__).parent.parent

# Find the .csv file relative to the project root and join to that path the data folder and then the example.csv file
    csv_file = project_root.joinpath('data', 'paralympics_raw.csv')
# csv_file = project_root / 'data' / 'example.csv' # this notation would also work, even though you think the '/' is only unix/macOS

# Check if the file exists, this will print 'true' if it exists
    print(csv_file.exists())

'''def activity2():
    data_file_csv = resources.files(data).joinpath("paralympics_raw.csv")

    paralympics_df = pd.read_csv(data_file_csv)'''

def activity2():
    project_root = Path(__file__).parent
    csv_file = project_root.joinpath('data', 'paralympics_raw.csv')
    df = pd.read_csv(csv_file)
    df.describe()

activity1()

