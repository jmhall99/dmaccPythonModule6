"""
Program: main.py
Author: Jeremy Hall
Last date modified: 10/05/2021

The purpose of this program is to validate input by sending it through an imported function.
"""

from more_functions.validate_input_in_functions import score_input

display_string = score_input('Test 1', 70)  # function call, store in a variable
print(display_string)  # print the result of the function

display_string = score_input('Test 2', -11)  # function call, store in a variable
print(display_string)  # print the result of the function

display_string = score_input('Test 3', 170)  # function call, store in a variable
print(display_string)  # print the result of the function

display_string = score_input('Test 4', 'abacab')  # function call, store in a variable
print(display_string)  # print the result of the function