def sum_consecutive_equal_digits(number):
    # Convert the number to a string for easy iteration
    num_str = str(number)

    # Initialize variables
    current_digit = None
    current_sum = 0

    # Iterate through each digit
    for digit in num_str:
        # Check if the current digit is the same as the previous one
        if digit == current_digit:
            print(digit)
            current_sum += int(digit)
        else:
            current_digit = digit

    return current_sum

def main():
    print(sum_consecutive_equal_digits(12234455))

main()
