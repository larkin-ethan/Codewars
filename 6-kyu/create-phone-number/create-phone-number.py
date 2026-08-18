def create_phone_number(n):
    """
    What I learned:

    You can set up a format string using {} values and then add .format(*n). That will add all of the values.
    It would look like this "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

    I could've also just used the same format idea but put the indexs in directly since we know it is always 10 values
    It would look like this f"({n[0]}{n[1]}{n[2]}) -{n[3]}......"
    """
    
    # Setup the output string with a opening parentheses
    # Then iterate through the list and check at the 3rd char and
    # add a closing parentheses and space
    # Then at the 6th char add a dash and then add the rest
    
    # Create output string starting with a parentheses
    output_str = "("
    
    # Iterate through the indexes
    for i in range(len(n)):
        # If it is index 2 or the 3rd number then add the closing parentheses
        if i == 2:
            output_str += f"{n[i]}) "
            continue
        # If it is index 5 or the 6th number then add the dash
        if i == 5:
            output_str += f"{n[i]}-"
            continue
        # Otherwise default to just adding the char
        output_str += f"{n[i]}"
        
    # Return the output string
    return output_str
    
        
