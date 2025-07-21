"""
The example for the open and close
"""

# Base class
class MakeUser:
    def __init__(self, name, title, salary):
        self._name = name
        self._title = title
        self._salary = salary

    def get_details(self):
        return f"{self._name} - {self._title} - ${self._salary}"


# Extended class: we ADD new functionality without modifying MakeUser
class PerformanceUser(MakeUser):
    def __init__(self, name, title, salary, performance):
        super().__init__(name, title, salary)
        self._performance = performance

    def get_details(self):
        base = super().get_details()
        return f"{base} | Performance: {self._performance}"


# Dictionary to simulate storage
mapper = {
    1: MakeUser("Abhi", "SDE", 100),
    2: MakeUser("Anny", "AE", 120),
    3: PerformanceUser("Tom", "SDE", 100, "A"),
    4: PerformanceUser("Cat", "SDE", 90, "B"),
    5: MakeUser("Dan", "SDE", 110)
}

# Use polymorphism
for user_id, user_obj in mapper.items():
    print(f"User {user_id}: {user_obj.get_details()}")
