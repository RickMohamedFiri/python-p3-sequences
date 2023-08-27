def print_fibonacci(length):
    fibonacci_sequence = [0, 1]  # Initialize the sequence with the first two Fibonacci numbers.

    while len(fibonacci_sequence) < length:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    print(fibonacci_sequence[:length])  # Print the first 'length' elements of the sequence.


print_fibonacci(8)