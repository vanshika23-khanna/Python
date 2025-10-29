#Q81. Demonstrate docstring for a function

def divide_numbers(numerator, denominator):
    """
    Divide two numbers and return the result.
    Parameters:
    numerator (float): The numerator of the division.
    denominator (float): The denominator of the division. Must not be zero.
    71
    Returns:
    float: The result of the division.
    Raises:
    ValueError: If the denominator is zero.
    """
    if denominator == 0:
        raise ValueError("Denominator must not be zero.")
    return numerator / denominator

print("\n\nThis program is executed by Vanshika Khanna , 0231BCA033")