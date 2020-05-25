import pytest
import ast
from tests import utils


def load_ast_tree(filename):
        try:
            with open(filename) as f:
                fstr = f.read()
                return ast.parse(fstr, filename=filename)
        except:
            return ast.parse("()")

# Create categorize_set_comprehension()
@pytest.mark.test_task1_module4
def test_task1_module4():
    cat_def_found = False

    try:
        for x in load_ast_tree('budget/Expense.py').body:
            if isinstance(x, ast.ClassDef):
                if x.name == 'Expenses':
                    for y in x.body:
                        if (isinstance(y, ast.FunctionDef) and
                                y.name == 'categorize_set_comprehension' and
                                y.args.args[0].arg=='self'):
                            cat_def_found = True
    except Exception as e:
            # print('iter e = ' + str(e))
            pass

    assert cat_def_found, 'Did you define the method `def categorize_set_comprehension(self)`?'

# Create necessary_expenses
@pytest.mark.test_task2_module4
def test_task2_module4():
    necessary_expenses_found = False
    necessary_expenses_checks_found = False

    try:
        for x in load_ast_tree('budget/Expense.py').body:
            if isinstance(x, ast.ClassDef):
                if x.name == 'Expenses':
                    for y in x.body:
                        if (isinstance(y, ast.FunctionDef) and
                                y.name == 'categorize_set_comprehension'):
                            for z in y.body:
                                assignments = utils.get_assignments_from_child(z)
                                print("assignments = " + str(assignments))
                                if 'necessary_expenses:x:x:self:list' in assignments[0]:
                                   necessary_expenses_found = True
                                   if ('x:category:Phone' in assignments[0] and
                                        'x:category:Auto and Gas' in assignments[0] and
                                        'x:category:Classes' in assignments[0] and
                                        'x:category:Utilities' in assignments[0] and
                                        'x:category:Mortgage'in assignments[0]):
                                        necessary_expenses_checks_found = True

    except Exception as e:
            # print('iter e = ' + str(e))
            pass

    assert necessary_expenses_found, 'Did you create the variable `necessary_expenses`?'
    assert necessary_expenses_checks_found, 'Did you assign `necessary_expenses` to a set comprehension with all of the category checks?'

# Create food_expenses
@pytest.mark.test_task3_module4
def test_task3_module4():
    food_expenses_found = False
    food_expenses_checks_found = False

    try:
        for x in load_ast_tree('budget/Expense.py').body:
            if isinstance(x, ast.ClassDef):
                if x.name == 'Expenses':
                    for y in x.body:
                        if (isinstance(y, ast.FunctionDef) and
                                y.name == 'categorize_set_comprehension'):
                            for z in y.body:
                                assignments = utils.get_assignments_from_child(z)
                                print("assignments = " + str(assignments))
                                if 'food_expenses:x:x:self:list' in assignments[0]:
                                   food_expenses_found = True
                                   if ('x:category:Groceries' in assignments[0] and
                                        'x:category:Eating Out' in assignments[0]):
                                        food_expenses_checks_found = True

    except Exception as e:
            # print('iter e = ' + str(e))
            pass

    assert food_expenses_found, 'Did you create the variable `food_expenses`?'
    assert food_expenses_checks_found, 'Did you assign `food_expenses` to a set comprehension with all of the category checks?'

# Create food_expenses
@pytest.mark.test_task4_module4
def test_task4_module4():
    unnecessary_expenses_found = False

    try:
        for x in load_ast_tree('budget/Expense.py').body:
            if isinstance(x, ast.ClassDef):
                if x.name == 'Expenses':
                    for y in x.body:
                        if (isinstance(y, ast.FunctionDef) and
                                y.name == 'categorize_set_comprehension'):
                            for z in y.body:
                                assignments = utils.get_assignments_from_child(z)
                                print("assignments = " + str(assignments))
                                if ('unnecessary_expenses:set:self:list' in assignments[0] and 
                                    'necessary_expenses' in assignments[0] and 
                                    'food_expenses' in assignments[0]):
                                    unnecessary_expenses_found = True


    except Exception as e:
            # print('iter e = ' + str(e))
            pass

    assert unnecessary_expenses_found, 'Did you create the variable `unnecessary_expenses`? It should be initialized to `set(self.list)` minus `necessary_expenses` minus `food_expenses`.'

# Create food_expenses
@pytest.mark.test_task5_module4
def test_task5_module4():
    return_found = False

    try:
        for x in load_ast_tree('budget/Expense.py').body:
            if isinstance(x, ast.ClassDef):
                if x.name == 'Expenses':
                    for y in x.body:
                        if (isinstance(y, ast.FunctionDef) and
                                y.name == 'categorize_set_comprehension'):
                            for z in y.body:
                                returns = utils.get_returns_from_child(z)
                                print("returns = " + str(returns))
                                if 'necessary_expenses:food_expenses:unnecessary_expenses' in returns:
                                    return_found = True


    except Exception as e:
            # print('iter e = ' + str(e))
            pass

    assert return_found, 'Did you return `[necessary_expenses, food_expenses, unnecessary_expenses]`?'