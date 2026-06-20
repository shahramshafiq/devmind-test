def calculate_factorial(n: int) -> int:
    """
    Calculates the factorial of a given non-negative integer.

    Args:
    n (int): The input number for which the factorial is to be calculated.

    Returns:
    int: The factorial of the input number.

    Raises:
    ValueError: If the input number is negative.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result