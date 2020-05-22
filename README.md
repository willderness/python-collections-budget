# Setup
1. ### Install python
    Install python3 per your OS instructions.

2. ### Setup a virtual environment with venv
   Create the venv: `python -m venv venv` 
   
   Activate the venv: `source venv/bin/activate`

3. ### Install requirements
   Run the following command to install the project’s required libraries:
    
    `python -m pip install -r requirements.txt`

# Module 1
## Count Purchases by Category
### Verify module: 
    To run tests run: pytest -k "module1" -s
    To run the file: python -m budget.UsingCounter
1. ### Import the Expense Module

    Last month’s spending data is in  `data/spending_data.csv`, which is a spreadsheet with 3 columns for - Location, Category, and amount. For example, the first row contains: `Alaska Air,Travel,-$115.75`. We want to analyze our spending habits in a few different ways.  In this module, we are going to read in this file and display the categories with the most purchases in a graph. 

   To read in the data, we’ll use the classes in the file named Expense.py. There are 2 classes -- Expense (which has a vendor, category, and amount) and Expenses (which has a list of type Expense and a sum of the amounts). Expenses also has a method read_expenses() which we’ll use to read the .csv file.

   To start, open the file named `FrequentExpenses.py` in the `budget` directory, and add `import Expense` to the top of the file. 

2. ### Read in the Spending Data
   Create a variable named expenses and set it equal to calling the Expenses() constructor. Then call the read_expenses() method on expenses and pass in the name of the file `data/spending_data.csv`. 

3. ### Create a List of the Spending Categories
   Create an empty list called spendingCategories. Then, create a for loop that iterates each Expense in the expenses. Inside the loop, we want to `append()` `expense.category` to `spendingCategories`.

4. ### Count Categories with a Counter Collection
   In order to use the Counter Collection, `import collections` at the top of the file. Then after the for loop, create a new variable called `spendingCounter` and set equal to passing `spendingCategories` to the `collections.Counter()` constructor.

   If you printed the Counter with print(spendingCategories), you would see the following output:
`Counter({'Eating Out': 8, 'Subscriptions': 6, 'Groceries': 5, 'Auto and Gas': 5, 'Charity': 2, 'Gear and Clothing': 2, 'Phone': 2, 'Travel': 1, 'Classes': 1, 'Freelance': 1, 'Stuff': 1, 'Mortgage': 1, 'Paycheck': 1, 'Home Improvements': 1, 'Parking': 1, 'Utilities': 1})`

   You can see it shows the category as the key and the number of times it was used as the value. With ‘Eating Out` as the most common expense which was done 8 times.
 
5. ### Get the Top 5 Categories
   We can get only the top 5 most common categories by calling the `most_common()` method on `spendingCounter` and passing in the value `5`. Set the result equal to a variable called `top5`.

6. ### Convert the Dictionary to 2 Lists
   If you’ve used the `zip()` function before it combines 2 iterables (for example, combines two lists into a list of tuples). We can also use `zip(*dictionary_variable)` to separate the keys and values of a dictionary into separate lists. Since we want to have 2 separate lists for the categories and their counts for the bar graph, let’s call `zip(*top5)` and set the result equal to two variables - `categories, count`. 

7. ### Plot the Top 5 Most Common Categories
   Add `import matplotlib.pyplot as plt` to the top of the file. Then at the end of the file, call `fig,ax=plt.subplots()` to initialize `fig` as the Figure, or top level container for our graph. And `ax` as the Axes, which contains the actual figure elements. 

8. ### Create the bar chart
   Next, call `ax.bar()` with the `categories` and `count` lists as parameters. To add a title, call ax.set_title() and pass in the string '# of Purchases by Category'.  

9. ### Display the graph
   Finally, to display the graph, call `plt.show()`.

   The resulting graph should be displayed:




# Module 2
## Create the BudgetList class to Display Overage Expenses
### Verify module: 
    To run tests run: pytest -k "module2" -s
    To run the file: python -m budget.BudgetList
1. ### Create the BudgetList class
   In the `budget` directory, open the `BudgetList.py` file. Inside that file, create a class called `BudgetList` with only `pass` inside the class for now.

2. ### Create the constructor
   Replace `pass` with a constructor that has two parameters - `self, budget`. Then initialize the following class variables: 
   - `self.budget` to the passed-in `budget`
   - `self.sum_expenses` to `0`
   - `self.expenses` to an empty list
   - `self.sum_overages` to `0`
   - `self.overages` to an empty list

3. ### Define the append method
   Define an append method that has two parameters - `self` and `item`. Put `pass` inside the method for now. 

4. ### Add items to expenses that are under budget
  Replace `pass` with an `if` statement that checks if `self.sum_expenses` plus the passed-in `item` is less than `self.budget`. Inside the `if` block, call `append()` on `self.expenses` and pass in `item`. Also inside the `if` block, add `item` to `self.sum_expenses`. 

5. ### Add items to overages that are over budget
  After the `if` block, add an `else` block that calls `append()` on `self.overages` and passes in `item`. Also, increase `self.sum_overages` by `item`. 

6. ### Define the __len__ method
   Define a method called `__len__` that takes in `self` as a parameter. Inside the method, return the sum of the length of `self.expenses` and the length of `self.overages`.

7. ### Define the main function
   After the BudgetList class, define a `main() function`. Inside of `main()`, create a `myBudgetList` variable and assign it to calling the `BudgetList` constructor with a budget argument of `1200`.

8. ### Import the Expense module
   Before we can use the Expense class to read in spending data, `import Expense` at the top of BudgetList.py

9. ### Read in the spending data file
   Next, create a variable named expenses and set it equal to calling the `Expense.Expenses()` constructor. On the next line, call the `read_expenses()` method on `expenses` and pass in the name of the file `data/spending_data.csv`. For this to work, we also need to `import Expense` at the top of the file.

10. ### Add the expenses to the BudgetList
    After reading the expenses, create a `for` loop that has an iterator called `expense` and loops through `expenses.list`. Inside the for loop, call `append()`, with `expense.amount` as an argument, on `myBudgetList`.

11. ### Print the Length of myBudgetList
    Call print() to print out the string 'The count of all expenses: ' concatenated with the length of myBudgList inside the print() call. Hint: Call the len() function with myBudgetList as an argument, then wrap that in a call to str() to convert to a string.

12. ### Tell Python to run the main function
    After the main function, create an `if` statement that checks if `__name__` is equal to `"__main__"`. If so, call `main()`.

    Now we can test that append() and len() are working for our BudgetList. Run `python BudgetList.py` and the output should be `"The count of all expenses: 37"`.

# Module 3
## Finish Making BudgetList an Iterable
### Verify module: 
    To run tests run: pytest -k "module3" -s
    To run the file: python -m budget.BudgetList
1. ### Create __iter__()
    Next, we want to create an iterator for BudgetList by implementing __iter__() and __next__() to iterate the expenses list first and then continue iterating the overages list. Once those are implemented and you can get an iterator from BudgetList, it will be an iterable. Inside the BudgetList class, at the bottom, define an __iter__ method that has self as a parameter. Put `pass` inside the body of the method for now. 

2. ### Finish __iter__()
   Inside `__iter__()`, remove `pass` and replace it with setting `self.iter_e` to calling the `iter()` constructor with `self.expenses` as an argument. On the next line, set `self.iter_o` to calling the `iter()` constructor with `self.overages` as an argument. Finally to finish the method, `return self`.

3. ### Create __next__()
    After the __iter__ method, define the method __next__() with `self` as a parameter. Put `pass` inside the body of the method for now. 

4. ### Finish __next__()
   Inside `__next__()`, remove `pass` and replace it with a `try:` block. Inside the `try:` block, `return` a call to `__next__()` on `self.iter__e`. On the next line add an except block, StopIteration as stop as the exception. Inside the except block, `return` a call to `__next__()` on `self.iter__o`. 

5. ### Test the iterable
   We can now test that BudgetList works as an iterable by using it in a for loop. In main(), after the print statement, create a `for` loop that has an iterator called `entry` and loops through `myBudgetList`. Inside the for loop, call print() with `entry` as an argument. 

   If we run `python BudgetList.py`, the output should be `"The count of all expenses: 37"` followed by each of the 37 amounts.

6. ### Import Matplotlib
   Now we want to show a bar graph comparing the expenses, overages, and budget totals. First, we need to add `import matplotlib.pyplot as plt` to the top of the file after `import Expense`. 

7. ### Create the figure and axes
   Then at the end of main(), call `fig,ax=plt.subplots()` to initialize `fig` as the Figure, or top level container for our graph. And `ax` as the Axes, which contains the actual figure elements. 

8. ### Create the list of labels
   Create a variable called `labels` and set it equal to a list with the following values: `'Expenses', 'Overages', 'Budget'`.

9. ### Create the list of values
   Create a variable called `values` and set it equal to a list with the following properties from `myBudgetList`: `sum_expenses`, `sum_overages`, and `budget`.

10. ### Create the bar graph
    Next, call `ax.bar()` with the `labels` and `values` lists as parameters. 

11. ### Set the title
    To add a title, call ax.set_title() and pass in the string 'Your total expenses vs. total budget'.

12. ### Show the figure
    Finally, to display the graph, call `plt.show()`. 
