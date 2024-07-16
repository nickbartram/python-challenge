# Import os and csv modules to help get file path and read csv file
import os
import csv

# Get os to find the current directory
current_dir = os.getcwd()

# Join the path to the .csv file
csvpath = os.path.join(current_dir, 'PyBank','Resources', 'budget_data.csv')

# Create months and sums counters
total_months = 0
total_sum = 0

# Create profit/loss and date lists
profit_loss = []
date = []

# Open the .csv file as a new variable 'budget file'
with open(csvpath) as budget_file:

    # Use csv module to read and seperate elements of the file
    csvreader = csv.reader(budget_file, delimiter=',')

    # Find and save the header
    header = next(csvreader)

    # Convert csvreader into a list, troubleshooted online and XLA
    csv_list = list(csvreader)

    # Loop through every row of the csv_list
    for row in csv_list:

        # Add its column 1 value ('Profit/Losses') to the total_sum counter
        total_sum += int(row[1])

        # +1 to total months counter
        total_months += 1

        # Save the value in column 1 ("Profit/Losses") to a list: 'profit_loss' 
        profit_loss.append(int(row[1]))

        # Save the value in column 0 ("Date") to a list: 'date'
        date.append(row[0])
    
# Save changes in Profit/Losses between every two rows in a variable:
# Subtract this rows profit_loss value from the next one's,
# Do it for every row except the last, to avoid comparing to a blank space
changes_profit_loss = [profit_loss[i+1] - profit_loss[i] for i in range(len(profit_loss)-1)]

# Get the average change by dividing the sum of all the changes, by the number of them
average_change = sum(changes_profit_loss) / len(changes_profit_loss)

# Round the average to 2 decimal places
round_average_change = round(average_change, 2)

# Save to a variable the greatest increase and decrease in 'Profit/Losses'
# Find the maximum and minimum values of changes_profit_loss
max_increase = max(changes_profit_loss)
max_decrease = min(changes_profit_loss)

# Find the date of the change by adding 1 to the max_increase
# Add one because of logic of changes list comprehension
max_date = date[changes_profit_loss.index(max_increase) + 1]
min_date = date[changes_profit_loss.index(max_decrease) + 1]

# Print the financial analysis results starting with the title
print("Financial Analysis")

# Print a dividing line
print("--------------------------------------------------")

# Print total months,sum, and average change
print(f"Total Months: {total_months}")
print(f"Total: ${total_sum}")
print(f"Average Change: ${round_average_change}")

# Print greatest increase and decrease and their dates
print(f"Greatest Increase in Profits: {max_date} (${max_increase})")
print(f"Greatest Decrease in Profits: {min_date} (${max_decrease})")

# Create a file in the analysis folder of PyBank
fin_analysis = os.path.join(current_dir, 'PyBank', 'analysis', 'financial_analysis.txt')

# Export results to a text file
# Open a new file to write in and save it to 'results'
with open(fin_analysis, 'w') as results:

    # Start writing, starting with the title and then moving to next line
    results.write(f"Financial Analysis\n")
    results.write("----------------------------------------------------------------\n")
    
    # Write total months, total, average change, greatest increase and decrease 
    results.write(f"Total Months: {total_months}\n")
    results.write(f"Total: {total_sum}\n")
    results.write(f"Average Change: {round_average_change}\n")
    results.write(f"Greatest Increase in Profits: {max_date} (${max_increase})\n")
    results.write(f"Greatest Decrease in Profits: {min_date} (${max_decrease})\n")






        

      

    










