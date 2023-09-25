from typing import List
def expression(num1: int, num2: int, num3: int) -> int:
    
    expression = [
                    num1+num2*num3,
                    num1*(num2+num3),
                    num1*num2*num3,
                    (num1+num2)*num3
                ]

    return max(expression)


