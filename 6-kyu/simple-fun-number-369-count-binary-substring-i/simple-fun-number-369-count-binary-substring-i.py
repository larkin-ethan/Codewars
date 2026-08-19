def count_binary(s1, s2):
    # Short circuit and check if the string is even in the test string
    # Then go and iterate through the word counting the number of times it is seen
    
    # Exit out early if it is not in the string
    if s1 not in s2:
        return 0
    
    # Set up variable for total count
    total_count = 0
    
    # Iterate through each index in the list making sure the length of s1 is buffer
    # Subtracting one makes sure you always have the length of the s1 left
    # since you are indexing you have to subtract 1 extra
    for i in range(len(s2) - (len(s1) - 1)):
        # Check if the substring of s2 is the same as s1 and up the counter
        if s1 == s2[i:i+(len(s1))]:
            total_count += 1
​
    # Return the counter
    return total_count