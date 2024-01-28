# Implementation of the algorithm in Python
def sum_of_evens(numList):

    total_sum = 0
    
    
    for number in numList:

        if number % 2 == 0:
            total_sum += number

    return total_sum

# Test the function
numbers = [1, 2, 3, 4, 5, 6]
result = sum_of_evens(numbers)
print("Sum of evens:", result)
