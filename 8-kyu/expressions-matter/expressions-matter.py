def expression_matter(a, b, c):
    # Compute all of the different variations
    # Then find the largest value
    
    # Setup the initial largest value as the first expression
    largest = a * (b + c)
    
    # Check all of the other variations and make sure it is not 
    # larger than the largest
    if a * b * c > largest:
        largest = a * b * c
    if a + (b * c) > largest:
        largest = a + (b * c)
    if (a + b) * c > largest:
        largest = (a + b) * c
    if a + b + c > largest:
        largest = a + b + c
​
    # Return the largest value
    return largest