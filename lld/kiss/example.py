"""
KISS stands for:

"Keep It Simple, Stupid"

Or more politely:

"Keep It Short and Simple"

The KISS principle is important because it helps developers avoid the pitfalls of over-engineering and premature optimization.

Improved Readability: Simple code is easier to read and understand, making it more accessible to other developers who may need to work with the codebase in the future.

Reduced Complexity: By keeping code simple, developers can reduce the overall complexity of the software, making it easier to maintain and debug.

Faster Development: Simple code can be written and tested more quickly, allowing developers to iterate and deliver features faster.

Enhanced Reliability: Simple code is less likely to contain bugs or unexpected behavior, leading to more reliable software.

"""

#one example -- 

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def is_even_better(num):
    return num % 2 == 0


