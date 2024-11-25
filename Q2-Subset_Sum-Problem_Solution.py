def subset_sum(numbers, target):
    """
    Solves the Subset Sum problem using backtracking.

    Time Complexity Analysis:
    - Worst case: O(2^N) where N is the number of elements
    - Each element has two choices: include or exclude
    - Creates a binary tree of depth N

    Space Complexity: O(N) for recursion stack

    Performance Factors:
    1. Input size (N) - exponential impact
    2. Target sum - larger targets may require deeper search
    3. Distribution of numbers - affects pruning effectiveness
    4. Order of numbers - sorting can improve early pruning

    Optimizations:
    1. Sort numbers in descending order for better pruning
    2. Early termination when current sum exceeds target
    3. Skip duplicate numbers (optional enhancement)
    4. Dynamic programming could be used for dense input sets
    """
    def backtrack(index, current_sum, current_subset):
        # Base cases
        if current_sum == target:
            return current_subset
        if index >= len(numbers) or current_sum > target:
            return None

        # Include current number
        result = backtrack(index + 1,
                           current_sum + numbers[index],
                           current_subset + [numbers[index]])
        if result:
            return result

        # Exclude current number
        return backtrack(index + 1, current_sum, current_subset)

    # Sort numbers in descending order for better pruning
    numbers.sort(reverse=True)

    # Start backtracking
    result = backtrack(0, 0, [])
    return result


# Example usage
numbers = [3, 34, 4, 12, 5, 2]
target = 9
result = subset_sum(numbers, target)
print(f"Found subset: {result}")
