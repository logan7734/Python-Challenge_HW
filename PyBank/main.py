import os
import csv

csv_path = os.path.join(current,'budget_data.csv')

#empty lists
Months = []
Profit_Losses = []
Profit_Change = []
counter = 0


with open (csv_path,'r') as csvfile:
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
        Profit_Change.append(Monthly_Change)
        #keep adding to get through all rows
        counter = counter + 1
    else:
        counter = counter + 1

#calculate net profits
Net = sum(Profit_Losses)

#Total Months
Total_Months = len(Months)

#Calculate Average Change
Average_Change = round(sum(Profit_Changes)/len(Profit_Changes),2)

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
