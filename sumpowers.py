"""
Given two numbers X and N
We find __"number of ways"__ X can be expressed as:
sum of n-th power of unique natural numbers.
"""


# Function to check power representations recursively
def count_sumpowers(x, n, curr_num = 1, curr_sum = 0):
    # Initialize number of ways to express x as n-th powers of different natural numbers
    results = 0
 
    # Calling power of curr_num (current_number) raised to n
    p = pow(curr_num, n)
    while (p + curr_sum < x):
        # Recursively check all greater values of curr_num 
        results += count_sumpowers(x, n, curr_num+1, p+curr_sum)
        curr_num += 1
        p = pow(curr_num, n)
 
    # If sum of powers is equal to x then increase the value of result.
    if (p + curr_sum == x):
        results += 1
 
    # Return the final result
    return results

if __name__ == '__main__':
    # Values of X and N (inputs) are defined here.
    print(count_sumpowers(x = 100, n = 2))