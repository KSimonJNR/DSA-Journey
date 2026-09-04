def linear_search(numbers, target):
    """
    Search for a target value by checking each element
    from left to right.

    Returns the index of the target if found.
    Returns -1 if the target is not found.
    """
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index

    return -1
