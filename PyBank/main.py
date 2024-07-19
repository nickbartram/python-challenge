# Import os and csv modules to help get file path and read csv file
import os
import csv

# Get os to find the current directory using the (__file__) attribute
# Xpert Learning Assistant helped with this code, and it's proved the most reliable
current_dir = os.path.dirname(os.path.abspath(__file__))

# Join the path to the .csv file, save to csvpath variable
csvpath = os.path.join(current_dir, 'Resources', 'budget_data.csv')

# Create months and sums counters
total_months = 0
total_sum = 0

# Create profit/loss, date, and profit_loss_difference lists
profit_loss = []
date = []
profit_loss_difference = []

# Open the .csv file as a new variable 'budget file'
with open(csvpath) as budget_file:

    # Use csv module to read and separate elements of the file
    csvreader = csv.reader(budget_file, delimiter=',')

    # Find and save the header
    header = next(csvreader)

    # Convert csvreader into a list
    csv_list = list(csvreader)

    # Loop through every row of the csv_list
    for month in csv_list:

        # Save the value in column 0 ("Date") to a list: 'date'
        date.append(month[0])

        # Add its column 1 value ('Profit/Losses') to the total_sum counter
        total_sum += int(month[1])

        # Save the value in column 1 ("Profit/Losses") to a list: 'profit_loss' 
        profit_loss.append(int(month[1]))

        # +1 to total months counter
        total_months += 1

# For every row in profit_loss list except the last...
for i in range(len(profit_loss)-1):

    # Subtract the current row's value from the next one to get the difference or change between the two
    difference = profit_loss[i + 1] - profit_loss[i]

    # Append this difference to the profit_loss_difference list
    profit_loss_difference.append(difference)

# Get the average difference: divide sum by length of list
difference_avg = sum(profit_loss_difference) / len(profit_loss_difference)
# Round the average to 2 decimal places
round_difference_avg = round(difference_avg, 2)

# Save to a variable the greatest increase and decrease in 'Profit/Losses'
# Find the maximum and minimum values of profit_loss_difference
greatest_increase = max(profit_loss_difference)
greatest_decrease = min(profit_loss_difference)

# Find the date of the change by adding 1 to the greatest_increase
# Add one because of logic of for loop above (it looks at the next row to find the difference)
max_date = date[profit_loss_difference.index(greatest_increase) + 1]
min_date = date[profit_loss_difference.index(greatest_decrease) + 1]

# Print the financial analysis results starting with the title
print("Financial Analysis")
# Print a dividing line
print("----------------------------")

# Print total months,sum, and average change
print(f"Total Months: {total_months}")
print(f"Total: ${total_sum}")
print(f"Average Change: ${round_difference_avg}")

# Print greatest increase and decrease and their corresponding dates
print(f"Greatest Increase in Profits: {max_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {min_date} (${greatest_decrease})")

# Create a file in the analysis folder of PyBank
fin_analysis = os.path.join(current_dir, 'analysis', 'financial_analysis.txt')

# Export results to a text file
# Open a new file to write in and save it to 'results'
with open(fin_analysis, 'w') as results:

    # Start writing, starting with the title and then moving to next line
    results.write(f"Financial Analysis\n")
    results.write("----------------------------\n")
    
    # Write total months, total, average change, greatest increase and decrease 
    results.write(f"Total Months: {total_months}\n")
    results.write(f"Total: {total_sum}\n")
    results.write(f"Average Change: {round_difference_avg}\n")
    results.write(f"Greatest Increase in Profits: {max_date} (${greatest_increase})\n")
    results.write(f"Greatest Decrease in Profits: {min_date} (${greatest_decrease})\n")




        

      

    










