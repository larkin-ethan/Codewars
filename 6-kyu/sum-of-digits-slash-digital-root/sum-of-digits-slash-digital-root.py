def digital_root(n):
    """
    What I learned:

    Instead of writing my own function, I could've just recalled digital_root. Effectively would've
    done the same thing in fewer lines. It would've prevented the need for the while loop and sum check though. 
    """

    
    # Check if it is one digit to start with
    # Then iterate through n getting each digit and adding it together
    # Then check if that number is greater than 10 and if it is run it again
    
    # Check if length is less than 2. This will cover 0 and 1. Return the original value.
    if n < 10:
        return n
    
    # Set sum equal to the sum of the initial digits
    sum = add_digits(n)
    
    # While the sum is greater than or equal to 10 or larger than 1 digit run 
    # the add_digits again on the previous sum
    while(sum >= 10):
        sum = add_digits(sum)
       
    # Return the sum after it is less than 10
    return sum
​
def add_digits(num):
    # Reset the total every run
    total = 0
    
    # Iterate through each digit in the number and add them together
    for dig in str(num):
        # Turn the string value back into a int then add it to the total
        total += int(dig)
    
    # Return the total
    return total
