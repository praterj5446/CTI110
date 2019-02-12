'''Sales Prediction Program
February 05, 2019
CTI-110 P2T1 - Sales Prediction
Jessica Prater'''

#Get the projected total sales.
total_sales = float(input ("Please enter the projected sales: "))

#Calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23

#display the profit.
print("The profit is $", format(profit, ",.2f"))
