import os
import csv

# Set the file path
folder_path = r"C:\Users\nbart.DESKTOP-3OF7M8N\Desktop\Data Analysis Class Materials\class_assignments\python-challenge\PyBank\Resources"

# change current folder to folder path
os.chdir(folder_path)

# confirm the folder
path = os.getcwd()

file_path = os.path.join(path, 'budget_data.csv')

print("budget.csv is found at: ", file_path)

# Verify the folder
# print("Current folder: ", current_folder)

# Create months and sums counters
total_months = 0
total_sum = 0

# Create profit/loss and date list
profit_loss = []
date = []


with open(file_path) as budget_file:

    #get csv module to read and seperate elements of the file
    csvreader = csv.reader(budget_file, delimiter=',')

    # Access and remove header from table
    next(csvreader)

    # Convert csvreader into a list
    csv_list = list(csvreader)

    # Count rows, sums up their totals, and, for every row... 
    for row in csv_list:

        # Add sum to total_sum
        total_sum += int(row[1])

        # Add 1 to months counter
        total_months += 1

        # Add to profit_loss list
        profit_loss.append(int(row[1]))

        # Add to date list
        date.append(row[0])
    
# Calculate the changes in Profit/Loss
changes = [profit_loss[i+1] - profit_loss[i] for i in range(len(profit_loss)-1)]

# Calculate the average change
average_change = sum(changes) / len(changes)

# Round the average to 2 decimal places
round_average_change = round(average_change, 2)

# Find the greatest increase and decrease in profits
max_increase = max(changes)
max_decrease = min(changes)

# Find the date of the change by adding 1 to the max_increase
# Add one because of logic of changes list comprehension
max_increase_date = date[changes.index(max_increase) + 1]
max_decrease_date = date[changes.index(max_decrease) + 1]

# Print the financial analysis results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_sum}")
print(f"Average Change: ${round_average_change}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")




