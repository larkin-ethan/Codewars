def find_outlier(integers):
    # Have a dictionary that stores all of the numbers under either even or odd
    # Then check to see which one only has one and return that one
    
    # Create a empty dictionary that has even and odd empty list in it
    even_odd_dict = {"odd": [], "even": []}
    
    # Iterate through the integers and put them in the correct place in the dict
    for num in integers:
        # Modulo 2 to check if it is even if it is equal to 0
        if num % 2 == 0:
            even_odd_dict["even"].append(num)
            continue
        even_odd_dict["odd"].append(num)
    
    
    # Check which list has 1 and return the element from that list
    if len(even_odd_dict["even"]) == 1:
        return even_odd_dict["even"].pop()
    
    return even_odd_dict["odd"].pop()