def solution(s):
    # Iterate through the string and check if the char is lower case
    # If it is then just add it to the output string if it is not then just 
    # add a space then the letter
    
    # Setup output string
    output_str = ""
    
    # Iterate through each char
    for char in s:
        # Check if the char is equal to the lowercase version of the char
        # If it is add the char to the output string and continue
        if char == char.lower():
            output_str += char
            continue
        # Otherwise default to adding a space and the char
        output_str += f" {char}"
    
    # Return output string
    return output_str