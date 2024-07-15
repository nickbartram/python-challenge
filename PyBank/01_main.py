# PyBank Instructions
# In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. 
# You will be given a financial dataset called budget_data.csv. 
# The dataset is composed of two columns: "Date" and "Profit/Losses".

# Your task is to create a Python script that analyzes the records to calculate each of the following values:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period

# import os and csv

import os
import csv

# get the current working directory
path = os.getcwd()

# now create the path again for some reason, truncated perhaps more efficient?
file_path = os.path.join('..', 'Resources', 'budget_data.csv')

# Make sure total_sum starts at 0
total_sum = 0

# A with statement to read the file path and save in variable as an object
with open(file_path) as budget_object:

    # Read the file and separate it
    csvreader = csv.reader(budget_object, delimiter=',')

    # Access and remove header (once .csv knows there's a header it will automatically compensate for it in later code)
    next(csvreader)

    # Convert csvreader into a list and save to a new variable
    csv_data = list(csvreader)
   
    for row in csv_data:

        total_sum += int(row[1])
    
    print(total_sum)




        

      

    










