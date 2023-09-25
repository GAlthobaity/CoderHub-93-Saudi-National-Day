from typing import List
def find_missing_number(n: int, numbers: List[int]) -> int:
    for number in range(1,n+1):
        if number not in numbers:
            return number    
