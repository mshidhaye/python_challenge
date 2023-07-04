import os

import csv

# Path to the CSV file
file_path = os.path.join(".", "Resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidates = {}
winner = ''
winner_votes = 0

# Read the CSV file
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header row
# Iterate over each row in the CSV
    for row in csvreader:
        # Count the total number of votes
        total_votes += 1

        # Get the candidate name from the row
        candidate_name = row[2]

        # Add the candidate to the dictionary if not already present
        if candidate_name not in candidates:
            candidates[candidate_name] = 0

        # Increment the candidate's vote count
        candidates[candidate_name] += 1

# Print the total number of votes
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Calculate and print the percentage of votes and total votes for each candidate
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

    # Determine the winner based on popular vote
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

with open("Analysis/Analysis.txt","w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")

    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------")
   