def duplicate_encode(word):
    # First make the input string all lower case
    # Then make a dictionary of the letters
    # Then go through the word and check the dictionary for
    # that letter and put a ( if it is a 1 and ) if it is 
    # anything greater than one
    
    # This works under the assumption that the word is all chars
    
    # Set up empty dictionary for letters and empty string for output string
    letter_dict = {}
    output_str = ""
    
    # Iterate through the lowercase version of the word to get each letter
    for char in word.lower():
        # Check if it is already in the dictionary and if it is add 1 if not create the key
        if char in letter_dict:
            letter_dict[char] += 1
        else:
            letter_dict[char] = 1
    
    # Iterate through the word again and check the dictionary see if the value 
    # is greater than 1 if so then it is ")" other wise it is "("
    for char in word.lower():
        if letter_dict[char] > 1:
            output_str += ")"
            continue   
        output_str += "("
    
    # Return the final results
    return output_str