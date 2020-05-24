import csv
import os

velection = os.path.join("Resources", "election_data.csv")

with open(velection, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    csvheader = next(reader)

    candidate = []
    votes = []
    name = [] 
    
    for row in reader:
        candidate.append(row[2])
    candidate_count = [[x, candidate.count(x)] for x in set(candidate)]
    
    for row in candidate_count:
        name.append(row[0])
        votes.append(row[1])
    
    candidate_zip = zip(name, votes)
    candidate_list = list(candidate_zip)

    winner = max(votes)
    
    for row in candidate_list:
        if row[1] == winner:
            winner_name = row[0]
 
total_votes = len(candidate) 

li_total = candidate.count('Li')
li_percent = li_total / total_votes

o_tooley_total = candidate.count("O'Tooley")
o_tooley_percent = o_tooley_total / total_votes

khan_total = candidate.count('Khan')
khan_percent = khan_total / total_votes

correy_total = candidate.count('Correy')
correy_percent = correy_total / total_votes

print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------')
print(f'Khan: {khan_percent:.1%} ({khan_total})')
print(f'Correy: {correy_percent:.1%} ({correy_total})')
print(f'Li: {li_percent:.1%} ({li_total})')
print(f"O'Tooley: {o_tooley_percent:.1%} ({o_tooley_total})")
print(f'-------------------------')
print(f'Winner: {winner_name}')
print(f'-------------------------')

file = open("Analysis/Results.txt","w")
file.write (f"Election Results"+"\n") 
file.write (f"-------------------------"+"\n")
file.write (f"Total Votes: {total_votes}"+"\n")
file.write (f"-------------------------"+"\n")
file.write (f"Khan: {khan_percent:.3%} ({khan_total})"+"\n")
file.write (f"Correy: {correy_percent:.3%} ({correy_total})"+"\n") 
file.write (f"Li: {li_percent:.3%} ({li_total})"+"\n")
file.write (f"O'Tooley: {o_tooley_percent:.3%} ({o_tooley_total})"+"\n")
file.write (f"-------------------------"+"\n")
file.write (f"Winner: {winner_name}"+"\n")
file.write (f"-------------------------"+"\n")