from binary_search import binary_search


def test_binary_search_finds_first_element():
    numbers = [10, 20, 30, 40, 50]

    assert binary_search(numbers, 10) == 0


def test_binary_search_finds_middle_element():
    numbers = [10, 20, 30, 40, 50]

    assert binary_search(numbers, 30) == 2


def test_binary_search_finds_last_element():
    numbers = [10, 20, 30, 40, 50]

    assert binary_search(numbers, 50) == 4


def test_binary_search_returns_minus_one_when_not_found():
    numbers = [10, 20, 30, 40, 50]

    assert binary_search(numbers, 35) == -1


def test_binary_search_works_with_empty_array():
    assert binary_search([], 10) == -1


def test_binary_search_works_with_one_element():
    assert binary_search([10], 10) == 0

    assert binary_search([10], 20) == -1