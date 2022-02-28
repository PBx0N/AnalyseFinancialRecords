import os
import csv

#set csv paths and output paths
csvpath = os.path.join("Resources", "budget_data.csv")
outputpath = os.path.join("Financial Analysis.txt")


#set variables
CountMonths = 1
TotalChanges = 0
MonthData = []
NetChangesData = [] 
NetChange = 0


#open and print csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Skip header row
    next(csvreader)
    
    CurrentRow = next(csvreader)
    Previous = int(CurrentRow[1])
    TotalProfitLoss = int(CurrentRow[1])

    for row in csvreader:
        MonthData.append(str(row[0]))
        CountMonths = CountMonths + 1
        TotalProfitLoss = TotalProfitLoss + int(row[1])
        CurrentRow = int(row[1])
        NetChangesData.append(int(NetChange))
        NetChange = CurrentRow - Previous
        Previous = CurrentRow
        TotalChanges = TotalChanges + NetChange

    #find average
    AverageChanges = "{:.2f}".format(float(TotalChanges)/(float(CountMonths)-1))

    #find max and min of the changes, one row removed hence minus one to match
    MaxChanges = max(NetChangesData)
    MinChanges = min(NetChangesData)
    MaxMonth = NetChangesData.index(max(NetChangesData))-1 
    MinMonth = NetChangesData.index(min(NetChangesData))-1

    print("Financial Analysis")
    print("-------------------------------------")
    print("Total Months: " + str(CountMonths))
    print("Total: $" + str(TotalProfitLoss))
    print("Average Change: $" + str(AverageChanges))
    print("Greatest Increase in Profits: " + str(MonthData[MaxMonth]) + " ($" + str(MaxChanges) + ")")
    print("Greatest Decrease in Profits: " + str(MonthData[MinMonth]) + " ($" + str(MinChanges) + ")")


#Print data out to text    
with open(outputpath, "w") as txt_file:
    txt_file.write("Financial Analysis")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Total Months: " + str(CountMonths))
    txt_file.write("\n")
    txt_file.write("Total: $" + str(TotalProfitLoss))
    txt_file.write("\n")
    txt_file.write("Average Change: $" + str(AverageChanges))
    txt_file.write("\n")
    txt_file.write("Greatest Increase in Profits: " + str(MonthData[MaxMonth]) + " ($" + str(MaxChanges) + ")")
    txt_file.write("\n")
    txt_file.write("Greatest Decrease in Profits: " + str(MonthData[MinMonth]) + " ($" + str(MinChanges) + ")")
 