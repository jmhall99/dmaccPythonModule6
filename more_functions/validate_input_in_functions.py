"""
Program: validate_input_in_functions.py
Author: Jeremy Hall
Last date modified: 10/05/2021

The purpose of this program is to validate input received from the main.py file.
"""

def score_input(test_name, test_score=-1, invalid_message='invalid test score!'):
    try:
        val = int(test_score)
    except ValueError:
        try:
            val = float(test_score)
        except ValueError:
            print(test_name + ' ' + 'ValueError encountered!')
    if test_score >= 0 and test_score <= 100:
        input = test_name + ' ' + str(test_score)
    else:
        input = test_name + ' ' + invalid_message
    return input
