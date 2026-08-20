def count_smileys(arr):
    # Iterate through the list and find the ones that look like they are valid
    
    # Set up smile count var
    smile_count = 0
    
    # Iterate through each smile
    for smile in arr:
        # Check if it is any of the different smile variations
        if smile.find(")") == True or smile.find("D") == True or \
           smile.find("~)") == True or smile.find("~D") == True or \
           smile.find("-)") == True or smile.find("-D") == True:
        
            # Add one to the count if it is
            smile_count += 1
      
    # Return the smile count
    return smile_count