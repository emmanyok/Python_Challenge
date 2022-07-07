from cgitb import text
import os
import csv

# path to csv
path_to_csv = os.path.join('..','PyPoll','Resources','election_data.csv')
path_to_txt = os.path.join('..','PyPoll','Analysis','analysis.txt')

#initialise variables to hold dictionaries
candidates = []
candidates_votes={}
totalvotes = 0
winning_count = 0

#get the datafrom csv
with open(path_to_csv,'r', encoding="utf-8") as election_data:
    # read data contents
    read_data = csv.reader(election_data, delimiter= ',')
    header = next(read_data)
    
    #loop through the rows

    for row in read_data:
        # get the total votes
        totalvotes= totalvotes + 1
        candidates_name= row[2]

        if candidates_name not in candidates:
           candidates.append(candidates_name)
           candidates_votes[candidates_name]= 0
        candidates_votes[candidates_name]= candidates_votes[candidates_name]+1    



#open txt file 
with open(path_to_txt,'w') as export_file:

    #combine all values in one variable
    summary = (
      f"Election Results\n"
      f"----------------------------\n"
      f"Total Votes: {totalvotes}\n"
    )  
    print(summary)
    export_file.write(summary)
  
    for x in candidates_votes:

     votes = candidates_votes.get(x)
     vote_percantage = round((votes/totalvotes) * 100, 2)

     if (votes > winning_count):
        winning_count = votes
        winning_candidates = x
     output= (f'{x}: {vote_percantage}% ({votes})\n')
     print(output)

     export_file.write(output)
    winning_summary = (
     f'-------------------------\n'
     f'Winner: {winning_candidates}\n'
     f'-------------------------\n'
     )   
    print(winning_summary)
    export_file.write(winning_summary)
  
