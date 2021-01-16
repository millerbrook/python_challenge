#PyPoll main page
import os
import csv

poll_csv = os.path.join("Resources", "election_data.csv")

with open(poll_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_file)

    #set up a dictionary: key is candidate, value is number of votes
    candidate_votes = {}

    #variable to count total votes
    totalvote = 0
    
    #going through rows, finding new candidates, incrementing total votes, incrementing individual votes
    for row in csv_reader:
        totalvote = totalvote + 1
        recognized = False
#        for candidate in candidate_votes():
        if row[2] in candidate_votes.keys():
          #  if row[2] == candidate:
            candidate_votes[row[2]] += 1 #candidate_votes[key] means value of Khan
           # recognized = True
            
        #if recognized == False:
        else:
            #newcandidate = row[2]
            candidate_votes[row[2]] = 1 #both creates key and assigns 1 vote to it

    #calculating percentages and organizing individual results        
    individualresults = {}
    for candidate, votes in candidate_votes.items():
        percent_vote = votes/totalvote
        percent_formatted = "{:.2%}".format(percent_vote)
        candidate_name = candidate
        individualresults[candidate_name] = [percent_formatted, votes]
        
    # print(individualresults)
    # print(totalvote)

output_path = os.path.join("Analysis", "results.txt")

resultfile = open(output_path, "w") 

toFile = f"Here are the candidates and vote totals: \n"
print(toFile)
resultfile.write(toFile + '\n')

for candidate, resultnumbers in individualresults.items():
    tot = resultnumbers.pop()
    pct = resultnumbers.pop()
    resultfile.write(str(candidate))
    print(str(candidate))
    resultfile.write(" :  \n")
    resultfile.write("\tPercent of total: " + str(pct) + '\n\tActual Votes: ' + str(tot) + '\n\n')
    print(("\tPercent of total: " + str(pct) + '\n\tActual Votes: ' + str(tot) + '\n\n'))
resultfile.write("\nTotal votes: " + str(totalvote))
print("Total votes: " + str(totalvote))

resultfile.close()