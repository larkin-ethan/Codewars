def array(string):
    # Check to make sure the string is at least 3 chars long or return NULL
    # Split it by the commas then remove the first and last values then put it back together
    
    # Split it up by the comma
    array = string.split(",")
    # NOTE: that this must me less than 3 because it will break the following operation
    if len(array) < 3:
        return
    # Pop off the first element
    array.pop(0)
    # Pop off the last element
    array.pop()
    
    # Check if there is now only one element
    if len(array) == 1:
        # Return the only element in the array
        return array[0]
    else:
        # Setup output string only if it is required
        output_str = ""
        # Add the first element to the string
        output_str += array[0]
​
    # For every element after the first element which has already been added
    # add a space then the number to the string
    for i in range(1, len(array)):
        output_str += f" {array[i]}"
    
    # Return the output string
    return output_str