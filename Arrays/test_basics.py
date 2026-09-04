from basics import (
    create_array,
    access_element,
    update_element,
    add_element,
    remove_element,
    traverse_array,
)


def test_create_array():
    assert create_array() == [10, 20, 30, 40, 50]


def test_access_element():
    numbers = create_array()

    assert access_element(numbers, 0) == 10
    assert access_element(numbers, 2) == 30


def test_update_element():
    numbers = create_array()

    update_element(numbers, 1, 25)

    assert numbers == [10, 25, 30, 40, 50]


def test_add_element():
    numbers = create_array()

    add_element(numbers, 60)

    assert numbers == [10, 20, 30, 40, 50, 60]


def test_remove_element():
    numbers = create_array()

    remove_element(numbers, 30)

    assert numbers == [10, 20, 40, 50]


def test_traverse_array():
    numbers = create_array()

    assert traverse_array(numbers) == [10, 20, 30, 40, 50]
