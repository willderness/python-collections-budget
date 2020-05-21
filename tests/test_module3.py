import pytest
import ast
from tests import utils
from budget import BudgetList
from os import path

def load_ast_tree(filename):
        try:
            with open(filename) as f:
                fstr = f.read()
                return ast.parse(fstr, filename=filename)
        except:
            return ast.parse("()")

# Create __iter__()
@pytest.mark.test_task1_module3
def test_task1_module3():
    iter_def_found = False

    try:
        for x in load_ast_tree('budget/BudgetList.py').body:
            if isinstance(x, ast.ClassDef):
                if x.name == 'BudgetList':
                    for y in x.body:
                        if (isinstance(y, ast.FunctionDef) and
                                y.name == '__iter__' and
                                y.args.args[0].arg=='self'):
                            iter_def_found = True
    except Exception as e:
            # print('iter e = ' + str(e))
            pass

    assert iter_def_found, 'Did you define the method `def __iter__(self)`?'

# Create __iter__()
@pytest.mark.test_task2_module3
def test_task2_module3():
    iter_def_found = False
    self_iter_e_found = False
    self_iter_o_found = False
    self_return_found = False

    try:
        for x in load_ast_tree('budget/BudgetList.py').body:
            if isinstance(x, ast.ClassDef):
                if x.name == 'BudgetList':
                    for y in x.body:
                        if (isinstance(y, ast.FunctionDef) and
                                y.name == '__iter__' and
                                y.args.args[0].arg=='self'):
                            iter_def_found = True
                            # for z in y.body:
                            assignments = utils.get_assignments_from_child(y)
                            returns = utils.get_returns_from_child(y)
                            if 'self:iter_e:iter:self:expenses' in assignments:
                                self_iter_e_found = True
                            if 'self:iter_o:iter:self:overages' in assignments:
                                self_iter_o_found = True
                            if 'self' in returns:
                                self_return_found = True
    except Exception as e:
            # print('iter e = ' + str(e))
            pass

    assert iter_def_found, 'Did you define the method `def __iter__(self)`?'
    assert self_iter_e_found, 'Did you assign `self.iter_e` to the iterator `iter(self.expenses)`?'
    assert self_iter_o_found, 'Did you assign `self.iter_o` to the iterator `iter(self.overages)`?'
    assert self_return_found, 'Did you return `self`?'

# Create __next__()
@pytest.mark.test_task3_module3
def test_task3_module3():
    next_def_found = False

    try:
        for x in load_ast_tree('budget/BudgetList.py').body:
            if isinstance(x, ast.ClassDef):
                if x.name == 'BudgetList':
                    for y in x.body:
                        if (isinstance(y, ast.FunctionDef) and
                                y.name == '__next__' and
                                y.args.args[0].arg=='self'):
                            next_def_found = True
    except Exception as e:
            # print('next e = ' + str(e))
            pass

    assert next_def_found, 'Did you define the method `def __next__(self)`?'

# Create __next__()
@pytest.mark.test_task4_module3
def test_task4_module3():
    next_def_found = False
    try_found = False
    exception_handler_found = False
    iter_e_next_found = False
    iter_o_next_found = False

    try:
        for x in load_ast_tree('budget/BudgetList.py').body:
            if isinstance(x, ast.ClassDef):
                if x.name == 'BudgetList':
                    for y in x.body:
                        if (isinstance(y, ast.FunctionDef) and
                                y.name == '__next__' and
                                y.args.args[0].arg=='self'):
                            next_def_found = True
                            # for z in y.body:
                            if (isinstance(y.body[0], ast.Try)):
                                try_found = True
                                returns = utils.get_returns_from_child(y.body[0])
                                if returns[0] == 'self:iter_e:__next__':
                                    iter_e_next_found = True
                                if (isinstance(y.body[0].handlers[0], ast.ExceptHandler) and
                                    y.body[0].handlers[0].type.id == 'StopIteration' and 
                                    y.body[0].handlers[0].name == 'stop'):
                                    exception_handler_found = True
                                    returns = utils.get_returns_from_child(y.body[0])
                                    if returns[1] == 'self:iter_o:__next__':
                                        iter_o_next_found = True
    except Exception as e:
            # print('next e = ' + str(e))
            pass

    assert next_def_found, 'Did you define the method `def __next__(self)`?'
    assert try_found, 'Do you have a `try` block?'
    assert iter_e_next_found, 'Inside the try block, did you call `__next__()` on `self.iter_e`?'
    assert exception_handler_found, 'Do you have an `except` block that defines `Stopiteration as stop`?'
    assert iter_o_next_found, 'Inside the except block, did you call `__next__()` on `self.iter_o`?'

# Create Expense.Expenses object
@pytest.mark.test_task5_module3
def test_task5_module3():

    for_mybudgetlist_found = False
    print_call_found = False

    try:
        for x in load_ast_tree('budget/BudgetList.py').body:
             if (isinstance(x, ast.FunctionDef) and
                    x.name == 'main'):
                for y in x.body:
                    if (isinstance(y, ast.For) and 
                        isinstance(y.iter, ast.Name) and 
                        y.iter.id == 'myBudgetList'):
                        for_mybudgetlist_found = True
                        calls = utils.get_calls_from_child(y)
                        print("iterable calls = " + str(calls))
                        if 'print:entry' in calls:
                            print_call_found = True
    except Exception as e:
            # print('for print e = ' + str(e))
            pass
    
    assert for_mybudgetlist_found, 'Did you create a for loop that iterates `expenses.list`?'
    assert print_call_found, 'Did you call `print(entry)`?'

# Import Matplotlib
@pytest.mark.test_task6_module3
def test_task6_module3():
    assert 'plt' in dir(BudgetList), 'Have you imported `matplotlib.pyplot` as `plt` ?'

    # Call plt.subplots() object
@pytest.mark.test_task7_module3
def test_task7_module3():

    fig_ax_tuple_found = False
    plt_subplots_call_found = False

    try:
        for x in load_ast_tree('budget/BudgetList.py').body:
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
    
    assert fig_ax_tuple_found and plt_subplots_call_found, 'Did you call assign a Tuple `fig,ax` to `plt.subplots`?'

# Assign labels []
@pytest.mark.test_task8_module3
def test_task8_module3():

    assign_labels_found = False
    correct_labels = False

    try:
        for x in load_ast_tree('budget/BudgetList.py').body:
            if (isinstance(x, ast.FunctionDef) and
                    x.name == 'main'):
                for y in x.body:
                    if (isinstance(y, ast.Assign) and 
                        isinstance(y.targets[0], ast.Name) and
                        y.targets[0].id == 'labels'):
                        assign_labels_found = True
                        if (y.value.elts[0].s == 'Expenses' and
                            y.value.elts[1].s == 'Overages' and
                            y.value.elts[2].s == 'Budget'):
                            correct_labels = True

    except Exception as e:
            # print('labels e = ' + str(e))
            pass

    assert assign_labels_found and correct_labels, 'Did you assign a variable named `labels` to `[\'Expenses\', \'Overages\', \'Budget\']`?'

# Assign values []
@pytest.mark.test_task9_module3
def test_task9_module3():

    assign_values_found = False
    correct_values = False

    try:
        for x in load_ast_tree('budget/BudgetList.py').body:
            if (isinstance(x, ast.FunctionDef) and
                    x.name == 'main'):
                for y in x.body:
                    if (isinstance(y, ast.Assign) and 
                        isinstance(y.targets[0], ast.Name) and
                        y.targets[0].id == 'values'):
                        assign_values_found = True
                        # print("y.value.elts[0].values.id = " + str(y.value.elts[0].value.id))
                        # print("y.value.elts[0].attr = " + str(y.value.elts[0].attr))
                        if (y.value.elts[0].value.id == 'myBudgetList' and y.value.elts[0].attr == 'sum_expenses' and
                            y.value.elts[1].value.id == 'myBudgetList' and y.value.elts[1].attr == 'sum_overages' and
                            y.value.elts[2].value.id == 'myBudgetList' and y.value.elts[2].attr == 'budget'):
                            correct_values = True


    except Exception as e:
            # print('values e = ' + str(e))
            pass

    assert assign_values_found and correct_values, 'Did you assign a variable named `values` to `[myBudgetList.sum_expenses, myBudgetList.sum_overages, myBudgetList.budget]`?'

# Call ax.bar()
@pytest.mark.test_task10_module3
def test_task10_module3():

    ax_bar_found = False
    correct_values = False

    try:
        for x in load_ast_tree('budget/BudgetList.py').body:
            if (isinstance(x, ast.FunctionDef) and
                    x.name == 'main'):
                for y in x.body:
                    if (isinstance(y, ast.Expr) and 
                        isinstance(y.value, ast.Call)):
                        if (hasattr(y.value.func, 'value') and
                            y.value.func.value.id == 'ax' and
                            y.value.func.attr == 'bar'):
                            ax_bar_found = True
                            call = utils.get_calls_from_child(x)
                            if ('ax:bar:labels:values:color:green:red:blue' in call):
                                correct_values = True


    except Exception as e:
            # print('ax.bar() e = ' + str(e))
            pass

    assert ax_bar_found, 'Did you call `ax.bar()`?'
    assert correct_values, 'Did you call `ax.bar()` with the following parameters: `labels, values, color=\'grb\'`?'

# Call ax.set_title()
@pytest.mark.test_task11_module3
def test_task11_module3():

    ax_set_title_found = False
    correct_value = False

    try:
        for x in load_ast_tree('budget/BudgetList.py').body:
            if (isinstance(x, ast.FunctionDef) and
                    x.name == 'main'):
                for y in x.body:
                    if (isinstance(y, ast.Expr) and 
                        isinstance(y.value, ast.Call)):
                        if(hasattr(y.value.func, 'value') and
                                y.value.func.value.id == 'ax' and
                                y.value.func.attr == 'set_title'):
                            ax_set_title_found = True
                            call = utils.get_calls_from_child(x)
                            if ('ax:set_title:Your total expenses vs. total budget' in call):
                                correct_value = True


    except Exception as e:
            # print('set_title e = ' + str(e))
            pass

    assert ax_set_title_found, 'Did you call `ax.set_title()`?'
    assert correct_value, 'Did you call `ax.bar()` with the following parameter: `\'Your total expenses vs. total budget\'`?'

# Call ax.set_title()
@pytest.mark.test_task12_module3
def test_task12_module3():

    plt_show_found = False
    correct_value = False

    try:
        for x in load_ast_tree('budget/BudgetList.py').body:
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