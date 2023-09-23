"""
Задача №2
Написать точно такую же процедуру, но в декларативном стиле

"""

numbers = [2, 8, 3, 9, 4]

def sort_list_imperative(numbers):
    numbers.sort()
    numbers.reverse()
    return numbers


print(sort_list_imperative(numbers)) 