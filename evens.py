def even_number_of_evens(numbers):
    if isinstance(numbers, list):
        evens = sum([1 for n in numbers if n % 2 == 0])

# REFACTOR THE CODE -  The sum function can be added to the evens so it replaces 
#                       the bellow function. evens was equal to 0 before
#        print(sum([1 for n in numbers if n % 2 == 0]))

#       for n in numbers:
#           if n % 2 == 0:
#                evens += 1

        return True if evens and evens % 2 == 0 else False

# REFACTOR THE CODE - The bellow function should be written as above once testing is completed
#        if evens:
#            return evens % 2 == 0
#        else:
#            return False

    else:
        raise TypeError("A list was not passed into this function")


if __name__ == '__main__':
    even_number_of_evens([2, 1, 4])

