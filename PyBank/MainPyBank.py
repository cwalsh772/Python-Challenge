import os
import csv

vbudget = os.path.join("Resources", "budget_data.csv")

with open(vbudget, newline="") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)   
    V = []
    months = []
    revenue_change = []

    for rows in csvreader:
        V.append(int(rows[1]))
        months.append(rows[0])
    

    for x in range(1, len(V)):
        revenue_change.append((int(V[x]) - int(V[x-1])))

    revenue_mean = sum(revenue_change) / len(revenue_change)
    total_months = len(months)
    greatest_increase = max(revenue_change)
    greatest_decrease = min(revenue_change)

    print("Financial Analysis")
    print(".................................................")
    print("Total months: " + str(total_months))
    print("Total: " + "$" + str(sum(V)))
    print("Average change:" + "$" +  "{:.2f}".format(float(revenue_mean)))
    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))
    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))


    file = open("Analysis/Results.txt","w")
    file.write("Financial Analysis" + "\n")
    file.write("................................................." + "\n")
    file.write("Total months: " + str(total_months) + "\n")
    file.write("Total: " + "$" + str(sum(V)) + "\n")
    file.write("Average change:" + "$" +  "{:.2f}".format(float(revenue_mean))+ "\n")
    file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase) + "\n")
    file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")
    file.close()

