def convert_palindromes(numbers):
    # Go through the list of numbers and reverse the number
    # Check if the reversed number is equal to the original num
    # Add a 1 if it is and 0 if it is not
    
    pal_arr = []
    
    for num in numbers:
        # Turn it into a string then reverse and compare to the string num
        if str(num)[::-1] == str(num):
            # Add a 1 and continue to the next number
            pal_arr.append(1)
            continue
        # Add a 0 if it is not the same
        pal_arr.append(0)
    
    # Return the array of results
    return pal_arr