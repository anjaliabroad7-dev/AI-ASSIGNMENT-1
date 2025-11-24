
def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

print(fibonacci(10))

def fibonacci(n):
    """
    Generate the Fibonacci sequence up to n positive integer terms.
    """
    if not isinstance(n, int):
        raise ValueError("n must be an integer.")
    if n <= 0:
        raise ValueError("n must be a positive integer.")

    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Example usage
print(fibonacci(10))