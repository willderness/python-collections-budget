import collections
import matplotlib.pyplot as plt # Remember need to pip install matplotlib
from . import Expense

expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')

spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)

# Use collection Counter to count how many purchases were in each category
spending_counter = collections.Counter(spending_categories)
print(spending_counter)
top5 = spending_counter.most_common(5)
print("Number of categories = " + str(spending_counter.__len__())) #len(spendingCounter)))
#print(top5)

# zip puts 2 lists into a dict, *zip does the reverse
categories, count = zip(*top5)

# Graph each spending category count as a bar chart
fig,ax=plt.subplots()
ax.bar(categories, count) #, color=[numpy.random.rand(3,) for _ in range(5)])
ax.set_title('# of Purchases by Category')
plt.show()