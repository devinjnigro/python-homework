from pathlib import Path
import csv
Path.cwd()
budget_data = Path('/Users/Devin/Desktop/Jupyter-Workspace/text_files/budget_data.csv')
total_months = 0
total = 0
pnl_list = []
date_list = []
change = []
greatest_increase = 0
greatest_decrease = 0

with open(budget_data, 'r') as file:
    csvreader = csv.reader(file, delimiter=",")
    csv_header = next(csvreader)
    
    for line in csvreader:
        total_months += 1
        months = str(line[0])
        pnl = int(line[1])
        total += pnl
        date_list.append(months)
        pnl_list.append(pnl)
        
    for x in range(len(pnl_list) - 1):
    # I subtracted 1 because the length of the change list would logically be 1 less than pnl_list
        difference = pnl_list[x + 1] - pnl_list[x]
        change.append(difference)
        
    for in_dec in change:
        if greatest_decrease == 0:
            greatest_decrease = in_dec
        elif in_dec < greatest_decrease:
            greatest_decrease = in_dec
        elif in_dec > greatest_increase:
            greatest_increase = in_dec
            
    avg_change = round(sum(change) / len(change),2)        
        
    increase_index = change.index(greatest_increase) + 1
    decrease_index = change.index(greatest_decrease) + 1
    # I added 1 to these indices because the change list is 1 less than the date_list.

    increase_date = date_list[increase_index]
    decrease_date = date_list[decrease_index]
    
print("Financial Analysis")    
print("---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")


output_path = '/Users/Devin/Desktop/python_homework/python-homework/PyBank/PyBank_Analysis.txt'
with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")    
    file.write("---------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total}\n")
    file.write(f"Average Change: ${avg_change}\n")
    file.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})\n")