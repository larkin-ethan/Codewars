def descending_order(num):
    # First the number needs to be turned into an array of strings
    # Then sorted and reversed
    # Then turned back into int
    # This works under the assumption that num will always be a valid number
    
    array_num = []
    output_str = ""
    
    # Get each number from the whole number and put it into an array of string numbers
    for str_num in str(num):
        array_num.append(str_num)
    
    # Sort and reverse the array of string numbers then make it back into a complete string
    for char in sorted(array_num)[::-1]:
        output_str += "".join(char)
    
    # Turn it back into an int
    return int(output_str)
    
        