def max_window_sum(arr, k):
    """
    Return (start_index, max_sum) of the contiguous subarray of length k
    with the maximum sum. If len(arr) < k, return None.
    """
    if k <= 0:
        raise ValueError("Window size k must be positive")

    n = len(arr)
    if n < k:
        return None

    # initial window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    max_index = 0

    # slide window
    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        if window_sum > max_sum:
            max_sum = window_sum
            max_index = i - k + 1

    return (max_index, max_sum)


def count_goal_windows(arr, k, goal):
    """
    Count number of contiguous subarrays of length k
    whose average is >= goal.
    """
    if k <= 0:
        raise ValueError("Window size k must be positive")

    n = len(arr)
    if n < k:
        return 0

    count = 0
    window_sum = sum(arr[:k])
    if window_sum / k >= goal:
        count += 1

    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        if window_sum / k >= goal:
            count += 1

    return count


def longest_rising_streak(arr):
    """
    Return the length of the longest strictly increasing contiguous streak.
    """
    if not arr:
        return 0

    longest = 1
    current = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            current += 1
            longest = max(longest, current)
        else:
            current = 1

    return longest
