# import modules
import os
import csv

# file path for csv
csv_file = os.path.join("Resources", "budget_data.csv")

# file path for text file to write to
text_file = os.path.join("analysis", "budget_data.txt")

# open csv file
with open(csv_file, "r") as file:
    csvreader = csv.reader(file)
    # skip header row
    header = next(csvreader)
    # intialize variables
    months = 0
    total = 0
    profitloss = []
    profitlossdif = []

    # loop through rows
    for row in csvreader:
        months += 1
        total += int(row[1])
        # put date and profit/loss in list
        profitloss.append([row[0],int(row[1])])
   
    # loop through profit/loss element (1) of profitloss list to find difference
    for i in range(1,len(profitloss)):
        profitlossdif.append(profitloss[i][1] - profitloss[i-1][1])
    
    # find average of profitloss difference
    average = round(sum(profitlossdif)/len(profitlossdif),2)
    
    # find the max and min profit loss difference
    maxpro = max(profitlossdif)
    minpro = min(profitlossdif)

    # find the max and min profit loss difference index and then use to find the date
    maxindex = profitlossdif.index(maxpro)
    maxdate = profitloss[maxindex+1][0]
    minindex = profitlossdif.index(minpro)
    mindate = profitloss[minindex+1][0]
    
    # print out results
    print("Financial Analysis")
    print("--------------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${average}")
    print(f"Greatest Increase in Profits: {maxdate} (${maxpro})")
    print(f"Greatest Decrease in Profits: {mindate} (${minpro})")

    # write to text file
    with open(text_file,'w') as txtfile:
        txtfile.writelines(["Financial Analysis\n",
                            "--------------------------------\n",
                            "Total Months: " + str(months) + "\n",
                            "Total: $" + str(total) + "\n",
                            "Average Change: $" + str(average) + "\n",
                            "Greatest Increase in Profits: " + str(maxdate) + " ($" + str(maxpro) + ")\n",
                            "Greatest Decrease in Profits: " + str(mindate) + " ($" + str(minpro) + ")\n"])

    
