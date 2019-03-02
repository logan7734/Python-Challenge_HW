import os
import csv
#####
csv_path = os.path.join("budget_data.csv")

#empty lists
Months = []
Profit_Losses = []
Profit_Change = []
counter = 0


with open (csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip header
    csv_header = next(csvreader)
    #Loop over
    for row in csvreader:
         #append to Months
         Months.append(row[0])
         #append to Profit_Losses 
         Profit_Losses.append(int(row[1]))

for row in Profit_Losses:
       if counter > 0:
        value_1 = Profit_Losses[(counter - 1)]
        value_2 = Profit_Losses[counter]
        #Calculate Monthly_Change = month2 - month1 or value_2 - value_1
        Monthly_Change = value_2 - value_1
        #Append to Profit_Change
        Profit_Change.appendgit(Monthly_Change)
        counter = counter + 1
else:
    counter = counter + 1

#calculate net profits
Net = sum(Profit_Losses)

#Total Months
Total_Months = len(Months)

#Calculate Average Change
Average_Change = sum(Profit_Change)

#Greatest Increase
Greatest_Increase = max(Profit_Losses)
#Greatest Decrease
Greatest_Decrease = min(Profit_Losses)

Increase = Profit_Losses.index(Greatest_Increase)
Decrease = Profit_Losses.index(Greatest_Decrease)

#Get the values at index_1 and index_2 in Months list
Month_1 = Months[Increase]
Month_2 = Months[Decrease]

#Initial print statements
print("Financial Analysis")
print("------------------------")

#Print Total Months
print(f"Total Months: ",Total_Months)

#Print Net Profits
print(f"Total: ${Net}")

#Print Average Change
print(f"Average Change: ${Average_Change}")

#Print Greatest Increase and Greatest Decrease
print(f"Greatest Increase in Profits: {Month_1} (${Greatest_Increase})")
print(f"Greatest Decrease in Profits: {Month_2} (${Greatest_Decrease})")

#csv

#with open(output_dest, 'w') as writefile:
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(Total_Months) + '\n')
    writefile.writelines('Total Revenue: $' + str(Net) + '\n')
    writefile.writelines('Average Revenue Change: $' + str(Average_Change) + '\n')
    writefile.writelines('Greatest Increase in Revenue: ' + Month_1 + ' ($' + str(Greatest_Increase) + ')'+ '\n')
    writefile.writelines('Greatest Decrease in Revenue: ' + Month_2 + ' ($' + str(Greatest_Decrease) + ')')

#opens the output file in r mode and prints to terminal
with open(output_dest, 'r') as readfile:
    print(readfile.read())
