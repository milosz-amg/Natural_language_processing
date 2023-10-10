from ctypes import sizeof
from datetime import datetime
import classes
import csv

employees = []
issuedinvoices = []
receivedinvoices = []

monthly_balance = [0]*12

# issued invoice +
# recieved invoice -
# employee salary -

with open("./employee.csv",'r') as f_employee:
    csvreader = csv.reader(f_employee)
    next(csvreader)
    for row in csvreader:
        new_employee = classes.Employee(row[0],row[1],int(row[2]))
        employees.append(new_employee)

with open("./IssuedInvoice.csv",'r') as f_IssuedInvoice:
    csvreader = csv.reader(f_IssuedInvoice)
    next(csvreader)
    for row in csvreader:
        new_IssuedInvoice = classes.IssuedInvoice(row[0],int(row[1]))
        d=datetime.strptime(new_IssuedInvoice.date, '%Y-%m-%d') 
        new_IssuedInvoice.date = d.month
        issuedinvoices.append(new_IssuedInvoice)

with open("./receivedinvoice.csv",'r') as f_receivedinvoice:
    csvreader = csv.reader(f_receivedinvoice)
    next(csvreader)
    for row in csvreader:
        new_receivedinvoice = classes.ReceivedInvoice(row[0],int(row[1]))
        d=datetime.strptime(new_receivedinvoice.date, '%Y-%m-%d') 
        new_receivedinvoice.date = d.month
        receivedinvoices.append(new_receivedinvoice)

for ri in receivedinvoices:
    monthly_balance[ri.date] += ri.amount

for ii in issuedinvoices:
    monthly_balance[ii.date] -= ii.amount

for em in employees:
    for mb in range(len(monthly_balance)):
        monthly_balance[mb] -= em.salary

# print(monthly_balance)

for i in range(len(monthly_balance)):
    print(i,": ",monthly_balance[i])

