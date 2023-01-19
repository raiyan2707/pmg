# Raiyan Uddin
# PMG Technical Assessment

import csv
import os

import pandas as pd


# function to check file format is suitable
def checkPath(file_path):
    if not os.path.exists(file_path):
        print("Error: File or directory not found: " + file_path)

    if os.stat(file_path).st_size == 0:
        print("Error: The file is empty: " + file_path)


# function to add filename column to a csv file
def addColumn(filepath):
    df = pd.read_csv(filepath)
    df["filename"] = os.path.basename(filepath)

    return df


def main():
    # list of csv files to be combined
    path_names = ['C:/tmp/accessories.csv', 'C:/tmp/clothing.csv', 'C:/tmp/household_cleaners.csv']
    for file_path in path_names:
        checkPath(file_path)

    # add filename column to each csv
    df1 = addColumn('C:/tmp/accessories.csv')

    df2 = addColumn('C:/tmp/clothing.csv')

    df3 = addColumn('C:/tmp/household_cleaners.csv')

    # combine the 3 csv files with the new column
    combined = df1.append(df2)
    combined = combined.append(df3)
    print(combined)
    # send df to a new csv file
    combined.to_csv('combined.csv')


if __name__ == '__main__':
    main()
