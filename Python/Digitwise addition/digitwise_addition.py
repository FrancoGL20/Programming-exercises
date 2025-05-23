# *Digitwise Addition
# Digitwise addition is a special kind of addition where instead of adding 1 normally to the number, it adds 1 to every digit of that number. If the digit is a 9, we replace it with a 10 without carrying over to the next digit.

# *Examples
# 123 -> 234
# 910 -> 1021
# 789 -> 8910
# Task
# Program a function that takes two numbers, n and k, and outputs the number of digits in n after applying Digitwise addition k times. Since the answer can be very large, return the answer modulo 1_000_000_007.

# Your solution is expected to be O(klogn).

# *Examples
# (9812, 2) -> 6
# # Explanation:
# # 9812 -> 10923 -> 211034 -> 6 digits

# (9899, 3) -> 8
# # Explanation:
# # 9899 -> 1091010 -> 21102121 -> 32213232 -> 8 digits

def digitwise_addition(n, k):
    # Test Constraints:
    # 1 <= n <= 10 ** 9
    # 1 <= k <= 10 ** 5
    # Expected Time Complexity: O(k * log(n))
    
    for _ in range(k):
        new_n=[str(int(digit)+1) for digit in str(n)]
        
    
    
    return 0