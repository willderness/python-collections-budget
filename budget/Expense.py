import csv
from datetime import datetime

class Expense():
    def __init__(self, date_str, vendor, category, amount):
        self.date_time = datetime.strptime(date_str, '%m/%d/%Y %H:%M:%S')
        self.vendor = vendor
        self.category = category
        self.amount = amount


class Expenses():
    def __init__(self):
        self.list = []
        self.sum = 0

    # Read in the December spending data, row[2] is the $$, and need to format $$
    def read_expenses(self,filename):
        with open(filename, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                if '-' not in row[3]:
                    continue
                amount = float((row[3][2:]).replace(',',''))
                self.list.append(Expense(row[0],row[1], row[2], amount))
                self.sum += amount


    def categorize_for_loop(self):
            necessary_expenses2 = set()
            food_expenses2 = set()
            unnecessary_expenses2 = set()
            for i in self.list:
                if (i.category == 'Phone'      or i.category == 'Auto and Gas' or 
                    i.category == 'Classes'  or i.category == 'Utilities' or 
                    i.category == 'Mortgage'): 
                    necessary_expenses2.add(i)
                elif(i.category == 'Groceries' or i.category == 'Eating Out'):
                    food_expenses2.add(i)
                else:
                    unnecessary_expenses2.add(i)
            
            return [necessary_expenses2, food_expenses2, unnecessary_expenses2]