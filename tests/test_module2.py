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

# Create class BudgetList
@pytest.mark.test_task1_module2
def test_task1_module2():
    class_found = False

    try:
        for x in load_ast_tree('budget/BudgetList.py').body:
            if isinstance(x, ast.ClassDef):
                if x.name == 'BudgetList':
                    class_found = True
                    
    except Exception as e:
            pass
    
    assert path.exists('budget/BudgetList.py'), 'Did you create a file named `BudgetList.py` in the `budget/` folder?'
    assert class_found, 'Did you create a `class BudgetList` in `BudgetList.py`?'


# Create __init__ and class variables
@pytest.mark.test_task2_module2
def test_task2_module2():
    args_found = False
    init_found = False

    self_budget_assign_found = False
    expenses_assign_found = False
    overages_assign_found = False

    try:
         for x in load_ast_tree('budget/BudgetList.py').body:
            if isinstance(x, ast.ClassDef):
                if x.name == 'BudgetList':
                    for y in x.body:
                        if (isinstance(y, ast.FunctionDef) and y.name == '__init__'):
                            init_found = True

                            if (y.args.args[0].arg == 'self' and y.args.args[1].arg == 'budget'):
                                args_found = True
                            child_assign = utils.get_assignments_from_child(y)
                            # BudgetList __init__ assignments = ['self:budget:budget', 'self:sum_expenses:0', 
                            # 'self:expenses', 'self:sum_overages:0', 'self:overages']
                            if ('self:budget:budget' in child_assign):
                                self_budget_assign_found = True
                            if ('self:sum_expenses:0' in child_assign and 'self:expenses' in child_assign):
                                expenses_assign_found = True
                            if ('self:sum_overages:0' in child_assign and 'self:overages' in child_assign):
                                overages_assign_found = True

    except Exception as e:
            pass
    
    assert init_found, 'Did you create the `__init__` method in the `BudgetList` class?'
    assert args_found, 'The `__init__` method should take `self` and `budget` as parameters.'
    assert self_budget_assign_found, 'Did you initialize `self.budget` to `budget` in `__init__`()?'
    assert expenses_assign_found, 'Did you initialize `sum_expenses` to 0 and `expenses` to an empty list in `__init__`()?'
    assert overages_assign_found, 'Did you initialize `sum_overages` to 0 and `overages` to an empty list in `__init__`()?'

# Create append()
@pytest.mark.test_task3_module2
def test_task3_module2():
    append_def_found = False

    try:
        for x in load_ast_tree('budget/BudgetList.py').body:
            if isinstance(x, ast.ClassDef):
                if x.name == 'BudgetList':
                    for y in x.body:
                        if (isinstance(y, ast.FunctionDef) and
                                y.name == 'append' and
                                y.args.args[0].arg=='self' and 
                                y.args.args[1].arg=='item'):
                            append_def_found = True                
    except Exception as e:
            # print('append e = ' + str(e))
            pass
    
    assert append_def_found, 'Did you define the method `def append(self, item)`?'


# Add expenses in append()
@pytest.mark.test_task4_module2
def test_task4_module2():

    append_def_found = False
    # if (self.sum_expenses+item < self.budget):
    self_found = False
    sum_expenses_found = False
    op_add_found = False
    lt_found = False
    self_budget_found = False

    # if body
    sum_exp_inc_found = False
    exp_append_item_found = False
    
    try:
        for x in load_ast_tree('budget/BudgetList.py').body:
            if isinstance(x, ast.ClassDef):
                if x.name == 'BudgetList':
                    for y in x.body:
                        if (isinstance(y, ast.FunctionDef) and
                                y.name == 'append' and
                                y.args.args[0].arg=='self' and 
                                y.args.args[1].arg=='item'):
                            append_def_found = True
                            # print("y.body = " + str(y.body))
                            for z in y.body:
                                if_statements = utils.get_if_statements_from_child(z)
                                # print("if_statements = " + str(if_statements))
                                if (isinstance(z, ast.If)):
                                    # test = Compare() part
                                    if (z.test.left.left.value.id == 'self'):
                                        self_found = True
                                    if (z.test.left.left.attr == 'sum_expenses'):
                                        sum_expenses_found = True
                                    if (isinstance(z.test.left.op, ast.Add)):
                                        op_add_found = True
                                    if (isinstance(z.test.ops[0], ast.Lt)):
                                        lt_found = True
                                    if (z.test.comparators[0].value.id == 'self' and
                                        z.test.comparators[0].attr == 'budget'):
                                        self_budget_found = True
                                    # for each in body = Compare() part

                                    for item in z.body:
                                        aug_assign = utils.get_augassignments_from_child(item)
                                        func_call = utils.get_calls_from_child(item)

                                        if ('self:sum_expenses:item' in aug_assign):
                                            sum_exp_inc_found = True
                                        if ('self:expenses:append:item' in func_call):
                                            exp_append_item_found = True


                                            
    except Exception as e:
            # print('append e = ' + str(e))
            pass
    
    assert append_def_found, 'Did you define the method `def append(self, item)`?'
    assert self_found and sum_expenses_found and op_add_found and lt_found and self_budget_found, 'Add an `if` statement that checks if `self.sum_expenses+item < self.budget`.'
    assert sum_exp_inc_found, 'Inside the if statement, did you call `self.sum_expenses += item`?'
    assert exp_append_item_found, 'Inside the if statement, did you call `self.expenses.append(item)`?'

# Add overages in append()
@pytest.mark.test_task5_module2
def test_task5_module2():

    append_def_found = False
    # else body
    sum_over_inc_found = False
    over_append_item_found = False
    
    try:
        for x in load_ast_tree('budget/BudgetList.py').body:
            if isinstance(x, ast.ClassDef):
                if x.name == 'BudgetList':
                    for y in x.body:
                        if (isinstance(y, ast.FunctionDef) and
                                y.name == 'append' and
                                y.args.args[0].arg=='self' and 
                                y.args.args[1].arg=='item'):
                            append_def_found = True
                            # print("y.body = " + str(y.body))
                            for z in y.body:
                                if_statements = utils.get_if_statements_from_child(z)
                                # print("if_statements = " + str(if_statements))
                                if (isinstance(z, ast.If)):
                                    for item in z.orelse:
                                        aug_assign = utils.get_augassignments_from_child(item)
                                        func_call = utils.get_calls_from_child(item)
                                        if ('self:sum_overages:item' in aug_assign):
                                            sum_over_inc_found = True
                                        if ('self:overages:append:item' in func_call):
                                            over_append_item_found = True                       
    except Exception as e:
            # print('append e = ' + str(e))
            pass
    
    assert append_def_found, 'Did you define the method `def append(self, item)`?'
    assert sum_over_inc_found, 'Inside the else statement, did you call `self.sum_overages+=item`?'
    assert over_append_item_found, 'Inside the else statement, did you call `self.overages.append(item)`?'

# Create __len__()
@pytest.mark.test_task6_module2
def test_task6_module2():
    len_def_found = False

    try:
        for x in load_ast_tree('budget/BudgetList.py').body:
            if isinstance(x, ast.ClassDef):
                if x.name == 'BudgetList':
                    for y in x.body:
                        if (isinstance(y, ast.FunctionDef) and
                                y.name == '__len__' and
                                y.args.args[0].arg=='self'):
                            len_def_found = True                
    except Exception as e:
            # print('__len__ e = ' + str(e))
            pass
    
    assert len_def_found, 'Did you define the method `def __len__(self)`?'
    # TODO test for return

# Create BudgetList object
@pytest.mark.test_task7_module2
def test_task7_module2():

    main_func_found = False
    budgetlist_assign_found = False
    try:
        for x in load_ast_tree('budget/BudgetList.py').body:
            if (isinstance(x, ast.FunctionDef) and
                    x.name == 'main'):
                main_func_found = True
                for y in x.body:
                    assignments = utils.get_assignments_from_child(y)
                    if 'myBudgetList:BudgetList:1200' in assignments:
                        budgetlist_assign_found = True

    except Exception as e:
            # print('next e = ' + str(e))
            pass
    
    assert main_func_found, 'Did you define a `main()` function?'
    assert budgetlist_assign_found, 'Did you define a `myBudgetList` variable assigned to `BudgetList(1200)`?'

# Import Matplotlib
@pytest.mark.test_task8_module2
def test_task8_module2():
    assert 'Expense' in dir(BudgetList), 'Have you imported `Expense`?'

# Create Expense.Expenses object
@pytest.mark.test_task9_module2
def test_task9_module2():

    expenses_assign_found = False
    read_expenses_call_found = False

    try:
        for x in load_ast_tree('budget/BudgetList.py').body:
            if (isinstance(x, ast.FunctionDef) and
                    x.name == 'main'):
                for y in x.body:
                    assignments = utils.get_assignments_from_child(y)
                    calls = utils.get_calls_from_child(y)
                    
                    if 'expenses:Expense:Expenses' in assignments:
                        expenses_assign_found = True
                    if 'expenses:read_expenses:data/spending_data.csv' in calls:
                        read_expenses_call_found = True

    except Exception as e:
            # print('next e = ' + str(e))
            pass

    assert expenses_assign_found, 'Did you define an `expenses` variable assigned to `Expense.Expenses()`?'
    assert read_expenses_call_found, 'Did you call `read_expenses(\'data/spending_data.csv\')` on `expenses`?'

# Append expenses
@pytest.mark.test_task10_module2
def test_task10_module2():

    for_expenses_found = False
    append_call_found = False

    try:
        for x in load_ast_tree('budget/BudgetList.py').body:
            if (isinstance(x, ast.FunctionDef) and
                    x.name == 'main'):
                for y in x.body:
                    if (isinstance(y, ast.For) and 
                        isinstance(y.iter, ast.Attribute) and 
                        y.iter.value.id == 'expenses' and
                        y.iter.attr == 'list'):
                        for_expenses_found = True
                        calls = utils.get_calls_from_child(y)
                        if 'myBudgetList:append:expense:amount' in calls:
                            append_call_found = True
                
    except Exception as e:
            # print('for_loop e = ' + str(e))
            pass
    
    assert for_expenses_found, 'Did you create a for loop that iterates `expenses.list`?'
    assert append_call_found, 'Did you call `append(n.amount)` on `myBudgetList`?'

# Print length of BudgetList
@pytest.mark.test_task11_module2
def test_task11_module2():
    print_call_found = False

    try:
        for x in load_ast_tree('budget/BudgetList.py').body:
            if (isinstance(x, ast.FunctionDef) and
                    x.name == 'main'):
                for y in x.body:
                    if (isinstance(y, ast.Expr) and 
                        isinstance(y.value, ast.Call) and
                        hasattr(y.value.func, 'id') and
                        y.value.func.id == 'print'):
                        calls = utils.get_calls_from_child(y)
                        # print("print calls = " + str(calls))
                        if 'print:The count of all expenses: :str:len:myBudgetList' in calls:
                            print_call_found = True
                
    except Exception as e:
            # print('for_loop e = ' + str(e))
            pass
    
    assert print_call_found, 'Did you print `\'The count of all expenses: \'` concatenated with `str(len(myBudgetList))`?'

# Run main
@pytest.mark.test_task12_module2
def test_task12_module2():
    main_call_found = False

    ifs = utils.get_if_statements(BudgetList)

    if '__name__:__main__:main' in ifs:
        main_call_found = True

    assert main_call_found, 'Did you add a conditional that checks if `__name__ == "__main__"` that runs `main()`?'