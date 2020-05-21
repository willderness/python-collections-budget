import matplotlib.pyplot as plt
from . import Expense

# Class that extends list type
class BudgetList():
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []
    
    def __len__(self):
        return (len(self.expenses) + len(self.overages))

    # implement append so that it only appends to self if total < budget
    def append(self, item):
        # TODO Check if item is a number
        if (self.sum_expenses+item < self.budget):
            self.expenses.append(item)
            self.sum_expenses += item
        # Otherwise append to the overages list and add to the overage total
        else:
            self.overages.append(item)
            self.sum_overages+=item

    # Create an iterable that combines self.expenses and self.overages
    # Create two local iterators for our internal lists using the default list iterator.
    def __iter__(self):
        self.iter_e = iter(self.expenses)
        self.iter_o = iter(self.overages)
        return self
    
    # Iterate first over the expenses iterator until it runs out, then switch to
    # the overages iterator. When it fails, it will return StopIteration to the caller.
    def __next__(self):
        try:
            return self.iter_e.__next__()
        except StopIteration as stop:
            return self.iter_o.__next__()

    
def main():
    # Using above class
    # Set starting budget to 500
    myBudgetList = BudgetList(1200)
    # Add expenses, the last expense is 100 and that goes in overages
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    for expense in expenses.list:
        myBudgetList.append(expense.amount)

    # Test len()
    print('The count of all expenses: ' + str(len(myBudgetList)))
    # Test out the iterable
    for entry in myBudgetList:
        print(entry)

    # Simple bar chart with Expenses total compared to Budget
    fig,ax=plt.subplots()
    labels = ['Expenses', 'Overages', 'Budget']
    values = [myBudgetList.sum_expenses, myBudgetList.sum_overages, myBudgetList.budget]
    ax.bar(labels, values, color=['green', 'red', 'blue'])
    ax.set_title('Your total expenses vs. total budget')
    plt.show()

if __name__ == "__main__":
    main()