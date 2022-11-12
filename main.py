# import everything needed
import os
import csv
# find path for csv file
budget_csv = os.path.join("Resources", "budget_data.csv")
# create lists to storage value
mon_change = []
profit_total = []
all_date = []
# set initial value
n_month = 0
net_profit = 0
change_profit = 0
first_profit = 0
# open and read file
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
# run file and get what is needed    
    for row in csv_reader:
        # calculate the total number of months
        all_date.append(row[0])
        n_month = n_month + 1
        # calculate net total amount of profit
    
        net_profit = net_profit + int(row[1])
        profit_total.append(row[1])
        # find the average of change
        last_profit = int(row[1])
        monthly_profit = last_profit - first_profit
        mon_change.append(monthly_profit)
        change_profit = change_profit + monthly_profit
        first_profit = last_profit
        avg_profit_change = (change_profit/n_month)
        # find 2 greatest
        in_profit = max(profit_total)
        de_loss = min(profit_total)
        in_date = all_date[profit_total.index(in_profit)]
        de_date = all_date[profit_total.index(de_loss)]
# print the result
    print("Financial Analysis")
    print("-"*20)
    print("Total Months: " + str(n_month))
    print("Total: " + "$" + str(net_profit))
    print("Average Change: " + "$" + str(avg_profit_change))
    print("Greatest Increase in Profits: " + str(in_date) + " ($" + str(in_profit) + ")")
    print("Greatest Increase in Profits: " + str(de_date) + " ($" + str(de_loss) + ")")