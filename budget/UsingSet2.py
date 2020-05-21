import timeit
import csv
import matplotlib.pyplot as plt
import Expense


expenses = Expense.Expenses()
expenses.read_expenses('spending_data.csv')
divided_list_comp = expenses.divide_expenses_list_comp()
divided_for_loop = expenses.divide_expenses_for_loop()

for i in range(len(divided_list_comp)):
    if not (divided_list_comp[i].union(divided_for_loop[i]) == divided_list_comp[i] and 
        divided_for_loop[i].union(divided_list_comp[i]) == divided_for_loop[i]):
        print("Sets are NOT equal by Union test")
        break

    if not (divided_for_loop[i].issubset(divided_list_comp[i]) and 
        divided_list_comp[i].issubset(divided_for_loop[i])):
        print("Sets are NOT equal by subset test")
        break
    

print(timeit.timeit(stmt = "expenses.divide_expenses_for_loop()",
                    setup=
                    '''
import Expense
expenses = Expense.Expenses()
expenses.read_expenses('spending_data.csv')
                    ''',
                    number=100000,
                    globals=globals()))

print(timeit.timeit(stmt = "expenses.divide_expenses_list_comp()",
                    setup=
                    '''
import Expense
expenses = Expense.Expenses()
expenses.read_expenses('spending_data.csv')
                    ''',
                    number=100000,
                    globals=globals()))

fig1, ax1 = plt.subplots()
labels = ['Necessary', 'Food', 'Unnecessary']
print("all_expenses_sum = " + str(expenses.sum))
divided_expenses_perc = []
for category_exps in divided_list_comp:
    divided_expenses_perc.append( sum(x.amount for x in category_exps) * 100 )

ax1.pie(divided_expenses_perc, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

plt.show()