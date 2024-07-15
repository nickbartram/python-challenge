import os
import csv

# Set the file path
# Going to need to be able to do this with a relative path but,
# Stuck so for now let's do the rest of it with this
folder_path = r"C:\Users\nbart.DESKTOP-3OF7M8N\Desktop\Data Analysis Class Materials\class_assignments\python-challenge\PyPoll\Resources"

# change current folder to folder path
os.chdir(folder_path)

# confirm the folder
path = os.getcwd()

file_path = os.path.join(path, 'election_data.csv')

# total votes, candidates votes, unique candidates

total_votes = 0
candidate_votes = {}
name = []




print("Election Results")
print("-------------------------------------------------------------")

# Open the file at the specified path
with open(file_path) as election_file:
    
    # Create csvreader variable, including the file seperated by a comma
    csvreader = csv.reader(election_file, delimiter=',')

    # Isolate the header
    next(csvreader)

    # Make sure python knows this is a list
    csvlist = list(csvreader)

    #Start a for loop to find all the candidates, this percentage of votes and total votes
    for row in csvlist:

        total_votes += 1

        candidate = row[2]

        if candidate not in name:

            name.append(candidate)
        
         # Count the votes for each candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
      
# Found items() method on Xpert Learning Assistant (henceforth: XLA)      
# for candidate, votes in candidate_votes.items():
    # print(f"{candidate}: {votes} votes")

for candidate in candidate_votes:
        
        votes = candidate_votes[candidate]

        percentage = (votes / total_votes) * 100

        round_percentage = round(percentage, 2)

        print(f"{candidate}: {round_percentage}% ({votes})")

print("----------------------------------------------------------------")

winner = max(candidate_votes, key=candidate_votes.get)

print(f"Winner: {winner}")


print("----------------------------------------------------------------")

