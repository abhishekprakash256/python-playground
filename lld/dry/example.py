"""
The dry principles means do not repeat yourself 

write the code that can be reused ---

"Every piece of knowledge must have a single, unambiguous, authoritative representation within a system."

It encourages us to minimize redundancy and write code that does one thing well, making our lives (and the lives of those who maintain our code) much easier.

Reduces code duplication

Makes code easier to maintain

Reduces bugs (fix in one place, applies everywhere)

Improves readability and reusability

"""


#the bad example 

# Violation: Duplicate logic
def get_area_of_square(side):
    return side * side

def get_area_of_rectangle(length, width):
    return length * width

def get_area_of_another_square(side):
    return side * side  # duplicate logic



# The correct example -- keeps the logic entact and no repetation of the code

def area_square(side):
    return side * side

def area_rectangle(length, width):
    return length * width

# Reuse the square function instead of repeating
def area_of_square_again(side):
    return area_square(side)


"""

DRY in Backend:

    Create utility functions, e.g. for date formatting, logging, etc.

    Use centralized config files

    Use inheritance or interfaces to avoid repeating logic

DRY in Frontend:

    Make reusable components (buttons, forms, etc.)

    Use layout templates

    Avoid copy-pasting JS/TS logic across components
"""