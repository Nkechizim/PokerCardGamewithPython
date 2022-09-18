def sum_of_list(numbers):
    """Return the sum of the numbers in a list.
    >>> sum_of_list([1, 2, 3])
    6
    >>> sum_of_list([6, 9, 4])
    19
    """
    total = 0
    for num in numbers:
        total += num
    
    return total

if __name__ == "__main__":
    import doctest
    doctest.testmod()