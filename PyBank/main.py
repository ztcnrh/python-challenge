import os
import csv

# Input path
budget_path = os.path.join('Resources', 'budget_data.csv')
# Output path
output_path = os.path.join('Analysis', 'results.txt')

## List variables
# "months" is used to retrieve "total months" and "greatest increase/decrease" months
# "p_l" is used to retrieve "total $ change"
# "changes" is used to retrieve "average $ change" and the "greatest increase/decrease in profits"
months = []
p_l = []
changes = []

# Read file
with open(budget_path, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    # Skip the header
    next(reader)

    # Loop over each row in the budget data
    for row in reader:
        # Increment the number of months to get the total
        months.append(row[0])
        # Append all "Profit/Loss" data as integers into a list
        p_l.append(int(row[1]))

# Loop through each recorded "Profit/Loss" in the budget data
for x in range(len(p_l) - 1):
    # Calculate month to month change
    change = p_l[x+1] - p_l[x]
    # Append all monthly changes to a list
    changes.append(change)
print(len(p_l))
# Calculate the average change
avg_change = sum(changes) / len(changes)

# Retrieve the correct index of the month with the greatest increase/decrease,
# and use the index to retrieve the correct month string from the "months" list
greatest_inc_index = changes.index(max(changes)) + 1
greatest_dec_index = changes.index(min(changes)) + 1
greatest_inc_month = months[greatest_inc_index]
greatest_dec_month = months[greatest_dec_index]


# Print the analysis to the terminal
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {len(months)}')
print(f'Total: ${sum(p_l)}')
print(f'Average Change: ${round(avg_change, 2)}')
print(f'Greatest Increase in Profits: {greatest_inc_month} (${max(changes)})')
print(f'Greatest Decrease in Profits: {greatest_dec_month} (${min(changes)})')


# Export a text file with the results by printing the same output into the file
with open(output_path, 'w') as text:
    print('Financial Analysis', file=text)
    print('----------------------------', file=text)
    print(f'Total Months: {len(months)}', file=text)
    print(f'Total: ${sum(p_l)}', file=text)
    print(f'Average Change: ${round(avg_change, 2)}', file=text)
    print(f'Greatest Increase in Profits: {greatest_inc_month} (${max(changes)})', file=text)
    print(f'Greatest Decrease in Profits: {greatest_dec_month} (${min(changes)})', file=text)


## ALTERNATIVE...
# with open(output_path, 'w') as text:
    # print('Financial Analysis\n'
    #     '----------------------------\n'
    #     f'Total Months: {len(months)}\n'
    #     f'Total: ${sum(p_l)}\n'
    #     f'Average Change: ${round(avg_change, 2)}\n'
    #     f'Greatest Increase in Profits: {greatest_inc_month} (${max(changes)})\n'
    #     f'Greatest Decrease in Profits: {greatest_dec_month} (${min(changes)})\n', file=text)