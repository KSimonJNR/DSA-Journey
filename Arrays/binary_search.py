def binary_search(numbers, target):
        """
            Search for a target value in a sorted array.

                Returns the index of the target if found.
                    Returns -1 if the target is not found.
                        """

        left = 0
        right = len(numbers) - 1

        while left <= right:
            middle = (left + right) // 2

            if numbers[middle] == target:
                return middle

            if numbers[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1