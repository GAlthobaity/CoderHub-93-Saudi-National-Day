from typing import List
def int_to_roman(num: int) -> str:
    roman_dict = {
        1:'I',
        4:'IV',
        5:'V',
        9:'IX',
        10:'X',
        40:'XL',
        50:'L',
        90:'XC',
        100:'C',
        400:'CD',
        500:'D',
        900:'CM',
        1000:'M'
    }

    roman = ""

    for intger, roman_equivlent in sorted(roman_dict.items(), reverse=True):
        while num >= intger:
            roman += roman_equivlent
            num -= intger
            
    return roman
