import math

def is_prime(n):
    """
    Checks if a number is prime.
    
    Args:
    n (int): The number to check.
    
    Returns:
    bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n < 0:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True