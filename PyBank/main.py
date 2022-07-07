import os
import csv

#initialise total month/ Profit/Losses
total_month = 0

#initialise values for changes
profit_losses = 0
total_change = []


# path to file
path_to_csv = os.path.join("..",'PyBank','Resources','budget_data.csv')
path_to_txt = os.path.join("..",'PyBank','Analysis','analysis.txt')

# converting csv data to a list of dictionary
with open(path_to_csv) as analysis_data:
    read_data = csv.reader(analysis_data)
    #skipping header row
    next(read_data, None)
    prev_change = 0

    #loop through the rows

    for row in read_data:
        total_month = total_month + 1
        #get the net of P & L
        profit_losses += int(row[1])        
        difference = int(row[1])-prev_change
        #set previous change
        prev_change = int(row[1])
        total_change.append(difference)


average_change = sum(total_change)/len(total_change)    
greatest_increase = max(total_change)
greatest_decrease = min (total_change)   

        


#print values
""" print(f"Financial Analysis\n")
print(f"----------------------------\n")
print(f"Total Months: {total_month}\n") 
print(f"Total: {profit_losses}\n") 
print(f"Average change: ${average_change}")
print(f"Greatest increase in profit: Aug-16 ({greatest_increase})\n")
print(f"Greater decrease in profit: Feb-14 ({greatest_decrease})\n")
 """

#combine all values in one variable
summary = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_month}\n" 
    f"Total: {profit_losses}\n"
    f"Average change: ${average_change}\n"
    f"Greatest increase in profit: Aug-16 ({greatest_increase})\n"
    f"Greater decrease in profit: Feb-14 ({greatest_decrease})\n"
    )

#print Summary variable
print(summary)

#Export Summary to text file
with open(path_to_txt, "w") as txt_file:
    txt_file.write(summary)