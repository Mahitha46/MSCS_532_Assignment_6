import random

# --------------------------------------------------------------
# Deterministic Median-of-Medians (Worst-case O(n))
# --------------------------------------------------------------

def median_of_medians(arr, k):
    """
    Deterministic selection algorithm (Median of Medians).
    Returns the k-th smallest element in arr (0-indexed).
    """

    if len(arr) <= 5:
        return sorted(arr)[k]

    # Step 1: Divide into groups of 5 and find medians
    medians = []
    for i in range(0, len(arr), 5):
        group = arr[i:i+5]
        medians.append(sorted(group)[len(group)//2])

    # Step 2: Recursively find the pivot median
    pivot = median_of_medians(medians, len(medians)//2)

    # Step 3: Partition around pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]

    # Step 4: Select based on ranks
    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + len(equal):
        return pivot
    else:
        return median_of_medians(high, k - len(low) - len(equal))


# --------------------------------------------------------------
# Randomized Quickselect (Expected O(n))
# --------------------------------------------------------------

def randomized_partition(arr, pivot):
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return less, equal, greater


def randomized_select(arr, k):
    """
    Randomized Quickselect algorithm.
    Returns the k-th smallest element in arr (0-indexed).
    """

    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)
    less, equal, greater = randomized_partition(arr, pivot)

    if k < len(less):
        return randomized_select(less, k)
    elif k < len(less) + len(equal):
        return pivot
    else:
        return randomized_select(greater, k - len(less) - len(equal))


# --------------------------------------------------------------
# RUN TESTS
# --------------------------------------------------------------

def run_tests():

    test_cases = [
        ([8, 3, 1, 7, 4, 9, 2], 3),
        ([10, 50, 30, 20, 40], 2),
        ([5, 1, 9, 3, 7, 2, 8, 6, 4], 4),
        ([100, 90, 80, 70, 60, 50], 1),
        ([12, 11, 13, 5, 6, 7], 0)
    ]

    print("==== SELECTION ALGORITHM TESTS ====\n")

    for i, (arr, k) in enumerate(test_cases, start=1):
        print(f"Test Case #{i}")
        print(f"Array: {arr}")
        print(f"k = {k}")

        det = median_of_medians(arr.copy(), k)
        rnd = randomized_select(arr.copy(), k)

        print(f"Deterministic Median-of-Medians Result: {det}")
        print(f"Randomized Quickselect Result: {rnd}")
        print("-" * 50)


# Run tests
run_tests()
