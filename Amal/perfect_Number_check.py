from typing import List
def perfect_Number_check(num):
    divisors_sum = sum([i for i in range(1, num) if num % i == 0])
    return num == divisors_sum


