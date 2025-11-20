class Employee:
    _base_salaries: dict[str, int] = {
        'trainee': 1000,
        'junior': 2000,
        'mid-level': 3000,
        'senior': 4000,
    }

    def __init__(self, name: str, level: str) -> None:
        if not (isinstance(name, str) and isinstance(level, str)):
            raise TypeError("'name' and 'level' attribute must be of type 'str'.")
        if level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{level}' for 'level' attribute.")

        self._name: str = name
        self._level: str = level
        self._salary: int = Employee._base_salaries[level]

    def __str__(self) -> str:
        return f'{self.name}: {self.level}'

    def __repr__(self) -> str:
        return f"Employee('{self.name}', '{self.level}')"

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise TypeError("'name' must be a string.")

        self._name = new_name
        print(f"'name' updated to '{self.name}'.")

    @property
    def level(self) -> str:
        return self._level

    @level.setter
    def level(self, new_level: str) -> None:
        if new_level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{new_level}' for 'level' attribute.")
        if new_level == self.level:
            raise ValueError(f"'{self.level}' is already the selected level.")
        if Employee._base_salaries[new_level] < Employee._base_salaries[self.level]:
            raise ValueError(f"Cannot change to lower level.")

        print(f"'{self.name}' promoted to '{new_level}'.")
        self.salary = Employee._base_salaries[new_level]
        self._level = new_level

    @property
    def salary(self) -> int:
        return self._salary

    @salary.setter
    def salary(self, new_salary: int) -> None:
        if not isinstance(new_salary, (int, float)):
            raise TypeError("'salary' must be a number.")
        if new_salary <= Employee._base_salaries[self.level]:
            raise ValueError(f'Salary must be higher than minimum salary ${Employee._base_salaries[self.level]}.')

        self._salary = new_salary
        print(f'Salary updated to ${self.salary}.')


charlie_brown = Employee('Charlie Brown', 'trainee')
print(charlie_brown)
print(f'Base salary: ${charlie_brown.salary}')
charlie_brown.level = 'junior'
