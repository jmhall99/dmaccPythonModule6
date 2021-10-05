"""
Program: inner_functions.py
Author: Jeremy Hall
Last date modified: 10/05/2021

The purpose of this program is to run values through some functions and get proper output
"""

def measurements(shape):
    x = shape[0]
    y = shape[1]

    def area(x, y):
        areaValue = x * y
        return areaValue

    area(x,y)

    def perimeter(x, y):
        perimeterValue = (x * 2) + (y * 2)
        return perimeterValue

    perimeter(x,y)

#I dont understand how to output the values from the two inner functions with the outer function.
#I did not see this in the material. Can you tell me where it is please?

output =  'perimeter = ' + perimeterValue + ' & area = ' + areaValue
return output


#the instructions say "in your main" call the function.   To me this means in MY main.py
#I find thuis very confusing

if __name__ == '__main__':      #this is NOT main.py I do not understand your explanation of this.
    rectangle = [2.1, 3.4]
    result = measurements(rectangle)
    print(result)
    square = [3.5, 3.5]
    result = measurements(square)
    print(result)



