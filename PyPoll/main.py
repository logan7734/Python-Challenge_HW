import os
import csv


csv_path = os.path.join("election_data.csv")

#empty lists
num_votes = []
candidates = []


with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        #append voter and candidates
        num_votes.append(row[0])
        candidates.append(row[2])

#Calculate Total Votes
Total_Votes = len(list(num_votes))

#counting votes per candidate 
Khan  = candidates.count("Khan")
Correy = candidates.count("Correy")
Li = candidates.count("Li")
OTooley = candidates.count("O'Tooley")

#Calculate percentage of votes 
Khan_Perc = round(((Khan/Total_Votes) * 100),3)
Correy_Perc = round(((Correy/Total_Votes) * 100),3)
Li_Perc = round(((Li/Total_Votes) * 100),3)
OTooley_Perc = round(((OTooley/Total_Votes) * 100),3)

#Print Election results and dotted line
print("Election Results")
print("-------------------------")

#print Total Votes
print(f"Total Votes: {Total_Votes}")

print("-------------------------")

#print results
print(f"Khan: {Khan_Perc}00% ({Khan})")
print(f"Correy: {Correy_Perc}00% ({Correy})")
print(f"Li: {Li_Perc}00% ({Li})")
print(f"O'Tooley: {OTooley_Perc}00% ({OTooley})")

print("-------------------------")

#print Winner
print("Winner: Khan")


print("-------------------------")
