# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python

def digital_root(n):
    number_string = str(n)
    total = 0
    
    while True:
        for num in number_string:
            total += int(num)
        
        if len(str(total)) == 1:
            break

        number_string = str(total)
        total = 0
    
    return total

import codewars_test as test
from solution import digital_root

@test.describe("Sum of Digits / Digital Root")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(digital_root(16), 7)
        test.assert_equals(digital_root(942), 6)
        test.assert_equals(digital_root(132189), 6)
        test.assert_equals(digital_root(493193), 2)