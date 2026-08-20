def high_and_low(numbers):
    # Turn it into a list of int then run max on the list and min on the list
    
    # Split the list by spaces
    numbers = numbers.split(" ")
    # Then turn them all into ints
    int_num = [int(num) for num in numbers]
​
    # Then return the max <space> min
    return f"{max(int_num)} {min(int_num)}"