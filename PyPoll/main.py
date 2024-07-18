# Import os and csv modules to help with getting the file path
import os
import csv

# Get the full path of the current directory and save it to a variable
current_dir = os.getcwd()

# Join the path together to form a full path to the .csv file
csvpath = os.path.join(current_dir, 'PyPoll', 'Resources', 'election_data.csv')

# Create a total_votes counter and start at zero
total_votes = 0

# Create a candidates_votes dictionary
candidates_tally = {}

# Create a names list
names = []

# Print the title of the results that will display in terminal
print("Election Results")
print("------------------------------------------------------")

# Open the .csv file and save it to a variable
with open(csvpath) as election_file:
    
    # Create csvreader variable, including the .csv file separated by a comma
    csvreader = csv.reader(election_file, delimiter=',')

    # Find and save the header
    header = next(csvreader)

    # Make sure the csvreader object is cast as a list
    csvlist = list(csvreader)

    # Start a for loop to find all the candidates, their percentage of votes and total votes
    for row in csvlist:

        # +1 to the total_votes tally
        total_votes += 1

        # Save the the name of the candidate (value in column 2)
        candidate = row[2]

        # If candidate is not already in the names list then...
        if candidate not in names:

            #... add candidate to the name list
            names.append(candidate)
        
         # Count the votes for each candidate
         # If the candidate is already in the candidates_tally dictionay then...
        if candidate in candidates_tally:
            
            #... +1 to the candidate votes
            candidates_tally[candidate] += 1

        # Otherwise set the votes to 1 because this is the first time
        else:
            candidates_tally[candidate] = 1
      

# Print total votes to the terminal
print(f"Total votes: {total_votes}")
print("------------------------------------------------------")

# Use each candidate's name to look through the candidate_votes dictionary
for candidate in candidates_tally:
        
        # Save the number of votes the candidate received to a variable
        votes = candidates_tally[candidate]

        # Divide each candidate's votes by the total votes and multiply by 100,
        # Save this percentage to a variable
        percentage = (votes / total_votes) * 100

        # Round the percentage to 2 decimal points and save to variable
        round_percentage = round(percentage, 2)

        # Print the candidate's name, their percentage of votes and total votes
        print(f"{candidate}: {round_percentage}% ({votes})")

# Print a dividing line
print("------------------------------------------------------")

# Find the winner
# Got help from stackoverflow (1) to find this method
# Use the max() method, with a specified key, to get that key's value
winner = max(candidates_tally, key=candidates_tally.get)

# Print the winner
print(f"Winner: {winner}")

# Print a dividing line
print("------------------------------------------------------")

# Create a file in the analysis folder of PyPoll
election_results = os.path.join(current_dir, 'PyPoll', 'analysis', 'election_results.txt')

# Open a new text file to write in, save it as a variable 'results'
with open(election_results, 'w') as results:

    # Write the title and start new line in the text file
    results.write("Election Results\n")
    results.write("-------------------------------------------------------\n")

    # Write the total votes and start new line
    results.write(f"Total votes: {total_votes}\n")
    results.write("-------------------------------------------------------\n")

    # Create a list comprehension
    # For every candidate in the candidates_tally dictionary...
    for candidate in candidates_tally:

        # Create a new votes variable to keep tally in this loop
        votes = candidates_tally[candidate]

        # Divide the candidates votes by the total votes and multiply by 100,
        # Save this percentage to a variable
        percentage = (votes / total_votes) * 100

        # Round the percentage to 2 decimal points and save to variable
        round_percentage = round(percentage, 2)
        # Write their name, vote percentage, total votes, and start a new line
        results.write(f"{candidate}: {round_percentage}% ({votes})\n")
    
    results.write("-------------------------------------------------------\n")

    # Write the winner and start new line
    results.write(f"Winner: {winner}\n")
    results.write("-------------------------------------------------------\n")
