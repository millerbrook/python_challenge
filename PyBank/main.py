#PyBank main page
#Parallel Lists Approach -- PyPoll's main.py uses a Dictionary-based 
# approach, here there are parallel lists

#Dependencies
import os
import csv

#Set up file reading
budget_pull_csv = os.path.join("Resources", "budget_data.csv")

#Establish initial variables
totalmonths = 0
net_profits = 0
months_list = []
monthly_profits_list = []
monthly_profits_total = 0
monthly_profits_mean = 0
last_month = 0
maxprofit = 0
maxmonth = ""
minprofit = 0
minmonth = ""

#Open CSV file
with open(budget_pull_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_file)
    #print(csv_header)
    #Read rows of CSV file
    for row in csv_reader:
        totalmonths += 1 #keeps track of total months
        
        if totalmonths == 1:#checks if we're on first row of data
            monthly_profits = "N/A" #assigns no profit or loss to first month
        else:
            monthly_profits = int(row[1]) - int(last_month) #calculates monthly profit
            net_profits = net_profits + int(row[1]) #adds up total profit/loss
            monthly_profits_total += int(monthly_profits) #adds new monthly profit/loss to total
       
        monthly_profits_list.append(monthly_profits) #appends monthly profit to list parallel to months list
        months_list.append(row[0]) #appends current month to months list
       
        if totalmonths > 1 and monthly_profits > maxprofit: #checks if current row is maximum profit
            maxprofit = monthly_profits #stores new Max Profit
            maxmonth = row[0] #assigns new max month
        elif totalmonths > 1 and monthly_profits < minprofit: #checks if current value is biggest loss
            minprofit = monthly_profits #assigns new biggest loss
            minmonth = row[0] #assigns new biggest loss month
        
        

    monthly_profits_mean = monthly_profits_total/(totalmonths-1) #out of loop, calc.s average of monthly profits

#Print everything to terminal
# ---------------------------
print(f"Financial Analysis\n---------------------\n")

print(f"Total Months: {totalmonths}\n")

print("Total: $" + format(net_profits, ',.2f') + "\n")

print(f"Average Change: $" + format(monthly_profits_mean, ',.2f') + "\n")

converted_loss = abs(minprofit)

print(f"Greatest Decrease in Profits: ($" + format(converted_loss, ',.2f') + f") (in {minmonth})\n")
 
print(f"Greatest Increase in Profits: $" + format(maxprofit, ',.2f') + f" (in {maxmonth}) \n")


#Write results to a text file
#-----------------------------  
output_path = os.path.join("Analysis", "results.txt")

resultfile = open(output_path, "w") 

resultfile.write(f"Financial Analysis\n---------------------\n")

resultfile.write(f"Total Months: {totalmonths}\n")

resultfile.write("Total: $" + format(net_profits, ',.2f') + "\n")

resultfile.write(f"Average Change: $" + format(monthly_profits_mean, ',.2f') + "\n")

resultfile.write(f"Greatest Decrease in Profits: ($" + format(converted_loss, ',.2f') + f") (in {minmonth})\n")
 
resultfile.write(f"Greatest Increase in Profits: $" + format(maxprofit, ',.2f') + f" (in {maxmonth}) \n")

resultfile.close()
