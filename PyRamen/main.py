import csv
from pathlib import Path
Path.cwd()
menu_filepath = Path('/Users/Devin/Desktop/Jupyter-Workspace/text_files/menu_data.csv')
sales_filepath = Path('/Users/Devin/Desktop/Jupyter-Workspace/text_files/sales_data.csv')
menu = []
sales = []

with open(menu_filepath, 'r') as menu_file:
    csvreader = csv.reader(menu_file, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        menu.append(row)

with open(sales_filepath, 'r') as sales_file:
    csvreader = csv.reader(sales_file, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        sales.append(row)

report = {}
row_count = 0

for row in sales:
    quantity = int(row[3])
    sales_item = str(row[4])
    
    if sales_item not in report:
        report[sales_item] = {}
        report[sales_item]["01-count"] = 0
        report[sales_item]["02-revenue"] = 0
        report[sales_item]["03-cogs"] = 0
        report[sales_item]["04-profit"] = 0
    
    for line in menu:
        item = str(line[0])
        price = float(line[3])
        cost = float(line[4])
             
        if item == sales_item:
            profit = quantity * (price - cost)
            report[sales_item]["01-count"] += quantity
            report[sales_item]["02-revenue"] += price * quantity
            report[sales_item]["03-cogs"] += cost * quantity
            report[sales_item]["04-profit"] += profit * quantity
        # I wasn't sure about the purpose of the else statement, and when I included it, it printed out thousands of lines.

    row_count += 1

print(report)

output_path = '/Users/Devin/Desktop/python_homework/python-homework/PyRamen/PyRamen_Analysis.txt'

with open(output_path, 'w') as file:
    file.write(str(report))