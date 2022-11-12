# import everything needed
import os
import csv
# find path for csv file
election_csv = os.path.join("Resources", "election_data.csv")
# create lists to storage value
can_list = []
name_can = []
vote_list = []
percent_list = []
# set initial value
n_vote = 0
# open and read file
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
# run file and get what is needed
    for row in csv_reader:
        # calculate the total number of ballot
        n_vote = n_vote + 1
        can_list.append(row[2])
    for x in set(can_list):
        # calculate the vote for each candidiate
        name_can.append(x)
        y = can_list.count(x)
        vote_list.append(y)
        percentage = (y/n_vote)*100
        percent_list.append(percentage)
    can1 = (name_can[0] + ": " + str(percent_list[0]) + "% (" + str(vote_list[0]) + ")")
    can2 = (name_can[1] + ": " + str(percent_list[1]) + "% (" + str(vote_list[1]) + ")")
    can3 = (name_can[2] + ": " + str(percent_list[2]) + "% (" + str(vote_list[2]) + ")")
    win_vote = max(vote_list)    
    winner = name_can[vote_list.index(win_vote)]


# print the result
print("Election Results")
print("-"*20)
print("Total Votes: " + str(n_vote))
print("-"*20)
print(can1)
print(can2)
print(can3)
print("-"*20)
print("The winner is: " + winner)
print("-"*20)