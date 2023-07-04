import os

import csv
from pathlib import Path

# csvpath = Path(".\Resources\cbudget_data.csv")
csvpath = os.path.join(".", "Resources", "cbudget_data.csv")
# Initialize variables
total_months = 0
net_profit_losses = 0
previous_profit_loss = 0
changes = []
greatest_increase = ['', 0]
greatest_decrease = ['', 0]

# Read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
                
# Skip header row
    header = next(csvreader)

    # Iterate over each row in the CSV file
    for row in csvreader:

        # Calculate the total number of months
        total_months += 1

        # Calculate the net total amount of "Profit/Losses"
        net_profit_losses += int(row[1])

        # Calculate the change in "Profit/Losses" from the previous month
        # if total_months > 1:
        current_profit_loss = int(row[1])
        change = current_profit_loss - previous_profit_loss
        changes.append(change)

        # Update the greatest increase in profits
        if change > greatest_increase[1]:
            greatest_increase = [row[0], change]

        # Update the greatest decrease in profits
        if change < greatest_decrease[1]:
            greatest_decrease = [row[0], change]

        previous_profit_loss = current_profit_loss

# Calculate the average change in "Profit/Losses"
changes.pop(0)
average_change = sum(changes) / len(changes)
# Print the calculated values
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

with open("Analysis/Analysis.txt","w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_profit_losses}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
