import pytest
import ast
from tests import utils
from budget import ExpenseCategories

def load_ast_tree(filename):
        try:
            with open(filename) as f:
                fstr = f.read()
                return ast.parse(fstr, filename=filename)
        except:
            return ast.parse("()")

# import timeit
@pytest.mark.test_task1_module5
def test_task1_module5():
    assert 'timeit' in dir(ExpenseCategories), 'Did you import `timeit`?'

# Call timeit
@pytest.mark.test_task2_module5
def test_task2_module5():
    found_timeit_call = False
    calls = utils.get_calls(ExpenseCategories)
    print("calls = " + str(calls))

    expected_timeit_str = 'timeit:timeit:stmt:pass:setup:\n:number:100000:globals:globals'
    expected_timeit_str_2 = 'timeit:timeit:stmt:expenses.categorize_for_loop():setup:\n from . import Expense\nexpenses = Expense.Expenses()\nexpenses.read_expenses(\'data/spending_data.csv\')\n:number:100000:globals:globals'

    for x in calls:
        if (expected_timeit_str in x.replace(" ", "") or 
            expected_timeit_str_2.replace(" ", "") in x.replace(" ", "")):
            found_timeit_call = True

    message = 'Did you call `timeit.timeit()`?'
    assert found_timeit_call, message

# Call timeit with actual code
@pytest.mark.test_task3_module5
def test_task3_module5():
    found_timeit_call = False
    calls = utils.get_calls(ExpenseCategories)
    print("calls = " + str(calls))

    expected_timeit_str = 'timeit:timeit:stmt:expenses.categorize_for_loop():setup:\n from . import Expense\nexpenses = Expense.Expenses()\nexpenses.read_expenses(\'data/spending_data.csv\')\n:number:100000:globals:globals'

    for x in calls:
        if expected_timeit_str.replace(" ", "") in x.replace(" ", ""):
            found_timeit_call = True

    message = 'Did you call `timeit.timeit()` and replace `stmt` and `setup` with the correct code?'
    assert found_timeit_call, message

# Call print(timeit)
@pytest.mark.test_task4_module5
def test_task4_module5():
    found_timeit_call = False
    calls = utils.get_calls(ExpenseCategories)
    print("calls = " + str(calls))

    expected_timeit_str = 'print:timeit:timeit:stmt:expenses.categorize_for_loop():setup:\n from . import Expense\nexpenses = Expense.Expenses()\nexpenses.read_expenses(\'data/spending_data.csv\')\n:number:100000:globals:globals'

    for x in calls:
        if expected_timeit_str.replace(" ", "") in x.replace(" ", ""):
            found_timeit_call = True

    message = 'Did you wrap the `timeit.timeit()` call with `print()`?'
    assert found_timeit_call, message

# Call print(timeit) again for set comprehension
@pytest.mark.test_task5_module5
def test_task5_module5():
    found_timeit_call = False
    calls = utils.get_calls(ExpenseCategories)
    print("calls = " + str(calls))

    expected_timeit_str = 'print:timeit:timeit:stmt:expenses.categorize_set_comprehension():setup:\n from . import Expense\nexpenses = Expense.Expenses()\nexpenses.read_expenses(\'data/spending_data.csv\')\n:number:100000:globals:globals'

    for x in calls:
        if expected_timeit_str.replace(" ", "") in x.replace(" ", ""):
            found_timeit_call = True

    message = 'Did you copy and paste the entire `print(timeit.timeit(...))` from the previous task and replace the `stmt` with `expenses.categorize_set_comprehension()`?'
    assert found_timeit_call, message

  # Call plt.subplots() object
@pytest.mark.test_task6_module5
def test_task6_module5():

    fig_ax_tuple_found = False
    plt_subplots_call_found = False

    try:
        for x in load_ast_tree('budget/ExpenseCategories.py').body:
             if (isinstance(x, ast.FunctionDef) and
                    x.name == 'main'):
                for y in x.body:
                    if (isinstance(y, ast.Assign) and 
                        isinstance(y.targets[0], ast.Tuple)):
                        if (y.targets[0].elts[0].id == 'fig' and 
                        y.targets[0].elts[1].id == 'ax'):
                            fig_ax_tuple_found = True

                            calls = utils.get_calls_from_child(y)
                            print("calls = " + str(calls))
                            if ('plt:subplots' in calls):
                                plt_subplots_call_found = True

    except Exception as e:
            # print('for print e = ' + str(e))
            pass
    
    assert fig_ax_tuple_found and plt_subplots_call_found, 'Did you assign a Tuple `fig,ax` to a call to `plt.subplots()`?'


# Assign labels []
@pytest.mark.test_task7_module5
def test_task7_module5():

    assign_labels_found = False
    correct_labels = False

    try:
        for x in load_ast_tree('budget/ExpenseCategories.py').body:
             if (isinstance(x, ast.FunctionDef) and
                    x.name == 'main'):
                for y in x.body:
                    if (isinstance(y, ast.Assign) and 
                        isinstance(y.targets[0], ast.Name) and
                        y.targets[0].id == 'labels'):
                        assign_labels_found = True
                        if (y.value.elts[0].s == 'Necessary' and
                            y.value.elts[1].s == 'Food' and
                            y.value.elts[2].s == 'Unnecessary'):
                            correct_labels = True

    except Exception as e:
            # print('labels e = ' + str(e))
            pass

    assert assign_labels_found and correct_labels, 'Did you assign a variable named `labels` to `[\'Necessary\', \'Food\', \'Unnecessary\']`?'

# Assign divided_expenses_sum
@pytest.mark.test_task8_module5
def test_task8_module5():
    assigns = utils.get_assignments(ExpenseCategories)
    print("assigns = " + str(assigns))

    assert 'divided_expenses_sum' in assigns, 'Did you create a variable `divided_expenses_sum` assigned to an empty list?'

# Sum each set's expenses
@pytest.mark.test_task9_module5
def test_task9_module5():
    fors = utils.get_for_loops(ExpenseCategories)
    print("fors = " + str(fors))
    found_for_loop = False

    for x in fors:
        if 'category_exps:divided_set_comp' in x:
            found_for_loop = True

    assert found_for_loop, 'Did you create a `for` loop that has an iterator called `category_exps` and loops through `divided_set_comp`?'
    assert ('category_exps:divided_set_comp:divided_expenses_sum:append:sum:x:amount:x:category_exps:0' in fors, 
           'Inside the for loop, did you call `divided_expenses_sum.append()`, with `x.amount for x in category_exps` as the argument?')

# Call ax.pie()
# ax.pie(divided_expenses_sum, labels=labels, autopct='%1.1f%%')
@pytest.mark.test_task10_module5
def test_task10_module5():

    ax_pie_found = False
    correct_values = False

    try:
        for x in load_ast_tree('budget/ExpenseCategories.py').body:
            if (isinstance(x, ast.FunctionDef) and
                    x.name == 'main'):
                for y in x.body:
                    if (isinstance(y, ast.Expr) and 
                        isinstance(y.value, ast.Call)):
                        if (hasattr(y.value.func, 'value') and
                            y.value.func.value.id == 'ax' and
                            y.value.func.attr == 'pie'):
                            ax_pie_found = True
                            call = utils.get_calls_from_child(y)
                            print("call = " + str(call))
                            if ('ax:pie:divided_expenses_sum:labels:labels:autopct:%1.1f%%' in call):
                                correct_values = True


    except Exception as e:
            print('ax.bar() e = ' + str(e))
            # pass

    assert ax_pie_found, 'Did you call `ax.pie()`?'
    assert correct_values, 'Did you call `ax.pie()` with the following parameters: `divided_expenses_sum, labels=labels, autopct=\'%1.1f%%\'`?'


# Call plt.show()
@pytest.mark.test_task11_module5
def test_task11_module5():

    plt_show_found = False

    try:
        for x in load_ast_tree('budget/ExpenseCategories.py').body:
            if (isinstance(x, ast.FunctionDef) and
                    x.name == 'main'):
                for y in x.body:
                    if (isinstance(y, ast.Expr) and 
                            isinstance(y.value, ast.Call)):
                        if(hasattr(y.value.func, 'value') and
                                y.value.func.value.id == 'plt' and
                                y.value.func.attr == 'show'):
                            plt_show_found = True

    except Exception as e:
            # print('plt.show() e = ' + str(e))
            pass

    assert plt_show_found, 'Did you call `plt.show()`?'