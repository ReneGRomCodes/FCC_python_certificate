class Category:
    """Represent a category for specific budget."""

    def __init__(self, name: str):
        """Initialize name, ledger and balance attributes."""
        self.name: str = name
        self.ledger: list[dict] = []
        self.balance: int = 0

    def __str__(self) -> str:
        """Return a formatted representation of the budget category, including ledger entries and the current
        balance."""
        # Set 'self.name' centered in between "*"s for a 30-character long title line.
        title_line_stars: str = (30 - len(self.name)) // 2 * "*"
        title_line: str = title_line_stars + self.name + title_line_stars
        if len(title_line) < 30:
            title_line = "*" + title_line
        budget: str = title_line + "\n"
        # Construct the ledger section in block style format.
        for position in self.ledger:
            # Restrict length of each line in ledger to 30 characters. Shorten description to do so if necessary.
            if len(position["description"]) + len(str(position["amount"])) >= 30:
                n = 30 - len(str(position["amount"])) - 1
                position["description"] = position["description"][:n]
            # Restrict length of description to 23 characters.
            if len(position["description"]) > 23:
                position["description"] = position["description"][:23]
            formatted_amount: str = "{:.2f}".format(position["amount"])
            length_space: str = (30 - (len(position["description"]) + len(formatted_amount))) * " "
            budget += position["description"] + length_space + formatted_amount + "\n"
        # Total budget.
        budget += f"Total: {self.balance:.2f}"
        return budget

    def deposit(self, amount: float, description: str="") -> None:
        """Take numeric value 'amount' and optional string 'description', insert them into 'self.ledger' and add
        'amount' to 'self.budget'."""
        self.ledger.append({"amount": amount,
                            "description": description,
                            })
        self.balance += amount

    def withdraw(self, amount: float, description: str="") -> bool:
        """Take numeric value 'amount' and optional string 'description', insert them into 'self.ledger' and subtract
        'amount' from 'self.budget' if sufficient funds are available. Return 'True' if withdrawal took place, 'False'
        if not."""
        check: bool = self.check_funds(amount)
        if check:
            self.ledger.append({"amount": amount * (-1),
                                "description": description,
                                })
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """Return numeric value for 'self.balance'."""
        return self.balance

    def transfer(self, amount: float, other_category: Category) -> bool:
        """Transfer numeric value 'amount' to instance 'other_category', update 'self.ledger' and 'self.budget' in each
        instance if sufficient funds are available and return 'True' if transfer took place, 'False' if not."""
        check: bool = self.check_funds(amount)
        if check:
            self.ledger.append({"amount": amount * (-1),
                                "description": "Transfer to " + other_category.name,
                                })
            other_category.ledger.append({"amount": amount,
                                          "description": "Transfer from " + self.name,
                                          })
            self.balance -= amount
            other_category.balance += amount
            return True
        else:
            return False

    def check_funds(self, amount: float) -> bool:
        """Check if numeric value 'amount' exceeds 'self.balance'. Return 'False' if it does and 'True' if not."""
        if amount > self.balance:
            return False
        else:
            return True


def get_expenses_amount(category: Category) -> int | float:
    """Take instance 'category', add all expenses and return them as positive numeric value 'expenses_amount'."""
    expenses_amount: int | float = 0
    for position in category.ledger:
        if position["amount"] < 0:
            expenses_amount -= position["amount"]

    return expenses_amount


def get_expenses_percent(categories: list[Category]) -> list:
    """Take a list of 'categories' and return a list of dictionaries containing the name of each category and the
    percentage (rounded down to the nearest 10) each category contributes to total expenses."""
    # Assign empty list 'expenses_percent' and variable 'exp_sum'.
    expenses_percent: list = []
    exp_sum: int | float = 0

    # Add all expenses from instances in 'categories'.
    for category in categories:
        expenses = get_expenses_amount(category)
        exp_sum += expenses

    # Calculate rounded down percentages and add them as dictionary to list 'expenses_percent' together with the name
    # of the category.
    for category in categories:
        exp_percentage_rounded = (((get_expenses_amount(category) / exp_sum) * 10) // 1) * 10
        expenses_percent.append({"category": category.name,
                                 "percentage": int(exp_percentage_rounded),
                                 })

    return expenses_percent


def get_line_percent(expenses: list, n: int) -> str:
    """Take list 'expenses' and value 'n' to build and return 'line' for spending chart. 'expenses' is a specific list
    of dictionaries created through 'get_expenses_percent()' function."""
    # Assign empty starting value for 'line'.
    line: str = ""

    # Build first section of 'line' based on value 'n'.
    if n == 100:
        line += "100| "
    elif n == 0:
        line += "  0| "
    else:
        line += " " + str(n) + "| "

    # Build second section of 'line' base on values extracted from list 'expenses'.
    for category in expenses:
        if category["percentage"] < n:
            line += "   "
        else:
            line += "o  "

    return line


def get_line_name(names: list[str], n: int) -> str:
    """Take list 'names' and value 'n' to build and return 'line' for spending chart."""
    # Create variable 'line' with multiple spaces to offset later additions to the right.
    line: str = "     "

    # Add character at index 'n' from each item in list 'names'. try-except clauses to avoid IndexError with shorter
    # names.
    for name in names:
        try:
            line += name[n] + "  "
        except IndexError:
            line += "   "

    return line


def create_spend_chart(categories: list[Category]) -> str:
    """Take list of instances 'categories', build a bar chart containing the name of each category and the percentage
    (rounded down to the nearest 10) each category contributes to total expenses."""
    # Assign starting values for 'chart', 'expenses_percent' and 'title_line'.
    chart: str = ""
    expenses_percent: list = get_expenses_percent(categories)
    title_line: str = "Percentage spent by category"

    # Build upper section of the bar chart including title, percentage, bars for percentages and a line dividing lower
    # section for category names.
    chart += title_line + "\n"
    for i in range(100, -1, -10):
        chart += get_line_percent(expenses_percent, i) + "\n"
    chart += "    -" + "---" * len(categories) + "\n"

    # Create list 'budget_names' to help build lower section of the chart.
    budget_names: list[str] = []
    for category in categories:
        budget_names.append(category.name)
    # Establish length of longest item in 'budget_names' for use in loops. '-1' is to account for offset and help avoid
    # empty last line.
    name_n = len(max(budget_names, key=len)) - 1
    # Build lower section of the chart, vertically aligning the names of each category.
    for i in range(0, name_n, 1):
        chart += get_line_name(budget_names, i) + "\n"
    chart += get_line_name(budget_names, name_n)

    return chart


# Instance, method and function calls to test functionality and outputs.
food = Category("FOOD")
clothing = Category("CLOTHING")
entertainment = Category("ENTERTAINMENT")
car = Category("CAR")

# Deposits.
food.deposit(1234.56, "First paycheck")
clothing.deposit(75, "Selling vintage jacket")
entertainment.deposit(99.99, "Concert tickets")
car.deposit(500, "Selling old stereo system")
food.deposit(777.77, "Lottery win")
# Withdrawals.
entertainment.withdraw(35.75, "Movie night")
food.withdraw(156.23, "Weekly groceries")
car.withdraw(112.88, "Car wash")
clothing.withdraw(62.50, "New jeans")
food.withdraw(234.89, "Dinner party")
# Transfers.
food.transfer(97.42, clothing)
clothing.transfer(48.67, entertainment)
car.transfer(88.91, food)
entertainment.transfer(22.34, car)

# Print budgets.
print(food)
print(clothing)
print(entertainment)
print(car)

# List of instances and testing of main function.
instances = [food, clothing, entertainment, car]
print(create_spend_chart(instances))
