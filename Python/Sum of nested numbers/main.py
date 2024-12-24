# *Task
# Build a function sum_nested_numbers that finds the sum of all numbers in a series of nested arrays raised to the power of their respective nesting levels. Numbers in the outer most array should be raised to the power of 1.

# For example,

# sum_nested_numbers([1, [2], 3, [4, [5]]])
# should return 1 + 2*2 + 3 + 4*4 + 5*5*5 === 149


def sum_nested_numbers(arr,m=1):
    total = 0
    for element in arr:
        if isinstance(element, int): 
            total += element**m
        else:
            total += sum_nested_numbers(element, m+1)
    return total


if __name__ == '__main__':
    pass