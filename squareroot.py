#This program takes a positive floating-point number as input and outputs an approx of it square root# 

def sqrt(x):
    def sqrt_iter(guess):             #variable#
        return guess if good_enough(guess) else sqrt_iter(improve(guess))
    def good_enough(guess):
        tolerance = 1e-3        # this will limit the margin for errors and provide the most accurate value#
        return abs(guess**2 - x) < tolerance
    def improve(guess):
        return (guess + x/guess)/2
    initial_guess = 1.0
    return sqrt_iter(initial_guess) 


positiveNumber = input ("Enter a positive number or enter/return to quit: ")

print(sqrt(positiveNumber))
