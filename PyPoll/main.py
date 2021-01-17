import os
import csv

input_path = os.path.join('Resources', 'election_data.csv')
output_path = os.path.join('Analysis', 'results.txt')

total_votes = 0
candidates_list = []
votes = []

# Read file
with open(input_path, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    # Skip the header
    header = next(reader)

    # Get total number of votes and a list of unique candidates
    for row in reader:
        total_votes += 1
        if row[2] not in candidates_list:
            candidates_list.append(row[2])

# Create a list of 0's with the number of candidates as the length to hold vote counts
for candidate in candidates_list:
    votes.append(0)


# Read file again to reset the pointer to the top row
with open(input_path, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    # Skip the header
    header = next(reader)

    # For each vote count index position, compare the candidate name in the input
    # file and the candidate name in the unique list of candidates, record the counts
    for row in reader:
        for candidate in range(len(candidates_list)):
            if row[2] == candidates_list[candidate]:
                votes[candidate] += 1

# Calculate each candidate's vote percentage
percentage = []
percentage = ['{:.3%}'.format(vote / total_votes) for vote in votes]

# Determine the winner based on vote count
for index, vote in enumerate(votes):
    if vote == max(votes):
        winner = candidates_list[index]

# Print the analysis to the terminal
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')
print(f'{candidates_list[0]}: {percentage[0]} ({votes[0]})')
print(f'{candidates_list[1]}: {percentage[1]} ({votes[1]})')
print(f'{candidates_list[2]}: {percentage[2]} ({votes[2]})')
print(f'{candidates_list[3]}: {percentage[3]} ({votes[3]})')
print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')


# Export a text file with the results by printing the same output into the file
with open(output_path, 'w') as text:
    print('Election Results', file=text)
    print('-------------------------', file=text)
    print(f'Total Votes: {total_votes}', file=text)
    print('-------------------------', file=text)
    print(f'{candidates_list[0]}: {percentage[0]} ({votes[0]})', file=text)
    print(f'{candidates_list[1]}: {percentage[1]} ({votes[1]})', file=text)
    print(f'{candidates_list[2]}: {percentage[2]} ({votes[2]})', file=text)
    print(f'{candidates_list[3]}: {percentage[3]} ({votes[3]})', file=text)
    print('-------------------------', file=text)
    print(f'Winner: {winner}', file=text)
    print('-------------------------', file=text)
