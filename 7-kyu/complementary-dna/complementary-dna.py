def DNA_strand(dna):
    # Switch all A into T and all C into G and vise versa
    # Iterate through the whole string and flip them as you go
    # There will be no emtpy strings and the assumption is made
    # that only valid dna chars will be used as input
    
    # Setup a place to store the complementary dna
    comp_dna = ""
    
    # Iterate through each char in the string and flip the dna
    for c in dna:
        if c == "A":
            comp_dna += "T"
        elif c == "T":
            comp_dna += "A"
        elif c == "C":
            comp_dna += "G"
        elif c == "G":
            comp_dna += "C"
        else:
            raise("Invalid DNA was recieved")
    
    # Return the complementary dna
    return comp_dna