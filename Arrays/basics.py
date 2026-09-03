# Basic Array Operations in Python
# My first DSA implementation


def create_array():
    """Create and return a sample array."""
    return [10, 20, 30, 40, 50]


def access_element(numbers, index):
    """Return an element at the given index."""
    return numbers[index]


def update_element(numbers, index, value):
    """Update an element and return the array."""
    numbers[index] = value
    return numbers


def add_element(numbers, value):
    """Add an element to the end of the array."""
    numbers.append(value)
    return numbers


def remove_element(numbers, value):
    """Remove an element from the array."""
    numbers.remove(value)
    return numbers


def traverse_array(numbers):
    """Return every element in the array."""
    return numbers


if __name__ == "__main__":
    numbers = create_array()

    print("Original array:", numbers)
    print("First element:", access_element(numbers, 0))

    update_element(numbers, 1, 25)
    print("After updating:", numbers)

    add_element(numbers, 60)
    print("After adding:", numbers)

    remove_element(numbers, 30)
    print("After removing:", numbers)

    print("Traversing array:")
    for number in traverse_array(numbers):
        print(number)
