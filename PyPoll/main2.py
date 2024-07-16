# Import os and csv modules to help with getting the file path
import os
import csv

# XLA help to discover the __file__ attribute
# Get the full path of the current file and save it to a variable
current_dir = os.path.dirname(os.path.realpath(__file__))

# Join the path together to form a full path to the .csv file
csvpath = os.path.join(current_dir, 'Resources', 'election_data.csv')

# Create a total_votes counter and start at zero
total_votes = 0

# Create a candidates_votes dictionary
nominee_votes_dict = {}

# Create a name list
names = []

# Print the title of the results that will display in terminal
print("Election Results")
print("-------------------------------------------------------------")

# Open the .csv file and save it to a variable
with open(csvpath) as election_file:
    
    # Create csvreader variable, including the .csv file seperated by a comma
    csvreader = csv.reader(election_file, delimiter=',')

    # Find and save the header
    header = next(csvreader)

    # Make sure python knows that csvreader is a list
    csvlist = list(csvreader)

    #Start a for loop to find all the candidates, this percentage of votes and total votes
    for row in csvlist:

        # +1 to the total_votes tally
        total_votes += 1

        # Save the the name of the nominee (value in column 2)
        nominee = row[2]

        # If candidate is not already in the name list then...
        if nominee not in names:

            #... add nominee to the name list
            names.append(nominee)
        
         # Count the votes for each candidate
         # If the nominee is already in the nominee_votes_dict dictionay then...
        if nominee in nominee_votes_dict:
            
            #... +1 to the nominee votes
            nominee_votes_dict[nominee] += 1

        # Otherwise set the votes to 1 because this is the first time
        else:
            nominee_votes_dict[nominee] = 1
      

# Print total votes to the terminal
print(f"Total votes: {total_votes}")
print("--------------------------------------------------------------")

# Use the candidate name to look through the candidate_votes dictionary
for nominee in nominee_votes_dict:
        
        # Save the number of votes the candidate received toa variable
        votes = nominee_votes_dict[nominee]

        # Divide the candidates votes by the total votes and multiply by 100,
        # Save this percentage to a variable
        percentage = (votes / total_votes) * 100

        # Round the percentage to 2 decimal points and save to variable
        round_percentage = round(percentage, 2)

        # Print the candidate's name, their percentage of votes and total votes
        print(f"{nominee}: {round_percentage}% ({votes})")

# Print a dividing line
print("----------------------------------------------------------------")

# Find the winner
# Got help from stackoverflow to find this method
# Use the max() method, with a specified key, to get that key's value
winner = max(nominee_votes_dict, key=nominee_votes_dict.get)

# Print the winner
print(f"Winner: {winner}")

# Print a dividing line
print("----------------------------------------------------------------")

# Open a new text file to write in, save it as a variable 'results'
with open('election_results.txt', 'w') as results:

    # Write the title and start new line in the text file
    results.write("Election Results\n")

    # Write a dividing line and start new line
    results.write("-------------------------------------------------------\n")

    # Write the total votes and start new line
    results.write(f"Total votes: {total_votes}\n")

     # Write a dividing line and start new line
    results.write("-------------------------------------------------------\n")

    # Create a list comprehension
    # For every nominee in the nominee_votes_dict dictionary...
    for nominee in nominee_votes_dict:

        # Write thier name, vote percentage, total votes, and start a new line
        results.write(f"{nominee}: {round_percentage}% ({votes})\n")

    # Write a dividing line and start new line
    results.write("-------------------------------------------------------\n")

    # Write the winner and start new line
    results.write(f"Winner: {winner}\n")

    # Write a final line and start new line
    results.write("-------------------------------------------------------\n")
