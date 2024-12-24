# *Task
# Consider a sequence of numbers a0, a1, ..., an, in which an element is equal to the sum of squared digits of the previous element. The sequence ends once an element that has already been in the sequence appears again.

# Given the first element a0, find the length of the sequence.

# *Example
# For a0 = 16, the output should be 9

# Here's how elements of the sequence are constructed:
# a0 = 16
# a1 = 1^2 + 6^2 = 37
# a2 = 3^2 + 7^2 = 58
# a3 = 5^2 + 8^2 = 89
# a4 = 8^2 + 9^2 = 145
# a5 = 1^2 + 4^2 + 52 = 42
# a6 = 4^2 + 2^2 = 20
# a7 = 2^2 + 0^2 = 4
# a8 = 42 = 16, which has already occurred before (a0)

# Thus, there are 9 elements in the sequence.

# For a0 = 103, the output should be 4

# The sequence goes as follows: 103 -> 10 -> 1 -> 1, 4 elements altogether.

# *Input/Output
# [input] integer a0
    # First element of a sequence, positive integer.
    # Constraints: 1 ≤ a0 ≤ 650.

# [output] an integer


def square_digits_sequence(n):
    """
    Generates a sequence where each number is the sum of the squares of the digits of the previous number.
    The sequence ends when a number repeats.
    
    Args:
        n (int): The starting number of the sequence.
    
    Returns:
        int: The length of the sequence until a number repeats.
    """
    sequence = [n]  # Stores the sequence of numbers
    while True:
        # Calculate the next number in the sequence
        next_number = sum(int(digit) ** 2 for digit in str(n))
        
        # Check if the next number is already in the sequence
        if next_number in sequence:
            return len(sequence) + 1
        
        # Append the next number to the sequence and update n
        sequence.append(next_number)
        n = next_number


if __name__ == '__main__':
    print(square_digits_sequence(16))
    print(square_digits_sequence(103))
    print(square_digits_sequence(104))
    print(square_digits_sequence(1))
    print(square_digits_sequence(86))
    print(square_digits_sequence(6))