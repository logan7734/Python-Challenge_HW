import os
import csv

#Join Current to csv file
csv_path = os.path.join('budget_data.csv')

#empty lists
Months = []
Profit_Loss = []
Profit_Change = []
count = 0

#open csv
with open (csv_path,'r') as csvfile:
    #read 
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip header
    csv_header = next(csvreader)
    #Loop over
    for row in csvreader:
         #append Months
         Months.append(row[0])
         #append to Profit_Loss
         Profit_Loss.append(int(row[1]))

#Loop over 
for row in Profit_Loss:
    if count > 0:
        #val_1: index prior to current row
        val_1 = Profit_Loss[(count - 1)]
        #val_2: is current iteration
        val_2 = Profit_Loss[count]
        #Calculate Monthly_Change = month2 - month1 or val_2 - val_1
        Monthly_Change = val_2 - val_1
        #Append to Profit_Change
        Profit_Change.append(Monthly_Change)
        #keep adding
        count = count + 1
    else:
            count = count + 1

Net = sum(Profit_Loss)

Total_Months = len(Months)

Average_Change = round(sum(Profit_Change)/len(Profit_Change),2)

Greatest_Increase = max(Profit_Loss)
Greatest_Decrease = min(Profit_Loss)


index_1 = Profit_Loss.index(Greatest_Increase)

index_2 = Profit_Loss.index(Greatest_Decrease)


Month_1 = Months[index_1]
Month_2 = Months[index_2]

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
output_path = os.path.join("bank_solved.csv")

with open(output_path, mode ='w', newline = '') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(['Financial Analysis\n'])
    csvwriter.writerow(['----------------------------' + '\n'])
    csvwriter.writerow(['Total Months: ' + str(Total_Months) + '\n'])
    csvwriter.writerow(['Total Revenue: $' + str(Net) + '\n'])
    csvwriter.writerow(['Average Revenue Change: $' + str(Average_Change) + '\n'])
    csvwriter.writerow(['Greatest Increase in Revenue: ' + Month_1 + ' ($' + str(Greatest_Increase) + ')'+ '\n'])
    csvwriter.writerow(['Greatest Decrease in Revenue: ' + Month_2 + ' ($' + str(Greatest_Decrease) + ')'])

#opens the output file in r mode and prints to terminal
with open(output_path, 'r') as readfile:
    print(readfile.read())

