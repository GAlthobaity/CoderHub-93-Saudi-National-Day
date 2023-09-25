from typing import List
def sum_numbers(num: int, s: str) -> int:
    if s == 'زوجي':
        return sum(number for number in range(2,num+1,2))
    else:
        return sum(number for number in range(1,num+1,2))
