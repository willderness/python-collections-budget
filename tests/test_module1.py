import pytest
import matplotlib
matplotlib.use('Agg')
from .utils import get_assignments, get_calls, get_for_loops
from budget import FrequentExpenses
from os import path

# import Expense
@pytest.mark.test_task1_module1
def test_task1_module1():
    assert path.exists('budget/FrequentExpenses.py'), 'Did you create a file named `FrequentExpenses.py` ?'
    assert 'Expense' in dir(FrequentExpenses), 'Have you imported the built-in `collections` library?'

# expenses = Expense.Expenses()
@pytest.mark.test_task2_module1
def test_task2_module1():
    assert 'expenses:Expense:Expenses' in get_assignments(FrequentExpenses), 'Do you have a `Expense.Expenses()` constructor call?'
    assert 'expenses:read_expenses:data/spending_data.csv' in get_calls(FrequentExpenses), 'Are you calling the `read_expenses()` method with `"data/spending_data.csv"`?'

# spending_categories = []
@pytest.mark.test_task3_module1
def test_spending_categories_init_module1():
    assert 'spending_categories' in get_assignments(FrequentExpenses), 'Are you initializing `spending_categories` to an empty list?'

    target_id_bool = get_for_loops(FrequentExpenses, 'dict')[0]['target:id'] == 'expense'
    iter_value_id_bool = get_for_loops(FrequentExpenses, 'dict')[0]['iter:value:id'] == 'expenses'
    iter_attr_bool = get_for_loops(FrequentExpenses, 'dict')[0]['iter:attr'] == 'list'
    message = 'Do you have a `for` loop that loops through the `expenses.list`?'
    assert target_id_bool and iter_value_id_bool and iter_attr_bool, message

    body_bool = get_for_loops(FrequentExpenses, 'dict')[0]['body'] == 'spending_categories:append:expense:category'
    message = 'Did you call `spendingCategories.append()` with `expense.category` inside the for loop?'
    assert body_bool, message

# import collections
@pytest.mark.test_task4_module1
def test_task4_module1():
    assert 'collections' in dir(FrequentExpenses), 'Have you imported the built-in `collections` library?'
    assert 'spending_counter:collections:Counter:spending_categories' in get_assignments(FrequentExpenses), 'Did you call `collections.Counter()` with argument `spendingCategories` and assign to `spendingCounter`?'

# top5 = spending_counter.most_common(5)
@pytest.mark.test_task5_module1
def test_task5_module1():
    assert 'top5:spending_counter:most_common:5' in get_assignments(FrequentExpenses), 'Did you call `spending_counter.most_common(5)` and assign to a variable `top5`?'

# categories, count = zip(*top5)
@pytest.mark.test_task6_module1
def test_task6_module1():
    assert 'categories:count:zip:top5' in get_assignments(FrequentExpenses), 'Did you call `zip(*top5)` and assign to variables `categories, count`?'

# import matplotlib
@pytest.mark.test_task7_module1
def test_task7_module1():
    assert 'plt' in dir(FrequentExpenses), 'Have you imported `matplotlib.pyplot` as `plt`?'
    assert 'fig:ax:plt:subplots' in get_assignments(FrequentExpenses), 'Did you call `plt.subplots()` and assign to variables `fig, ax`?'

# fig,ax=plt.subplots()
@pytest.mark.test_task8_module1
def test_task8_module1():
    # ax.bar(categories, count)
    assert 'ax:bar:categories:count' in get_calls(FrequentExpenses), 'Did you call `ax.bar()` with arguments `categories, count`?'
    # ax.set_title('# of Purchases by Category')
    assert 'ax:set_title:# of Purchases by Category' in get_calls(FrequentExpenses), 'Did you call `ax.set_title()` with argument `"# of Purchases by Category"`?'

@pytest.mark.test_task9_module1
def test_task9_module1():
    # plt.show()
    assert 'plt:show' in get_calls(FrequentExpenses), 'Did you call `plt.show()`?'
    # print(get_calls(FrequentExpenses))


