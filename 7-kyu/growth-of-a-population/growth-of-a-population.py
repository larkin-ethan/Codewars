import math # Needed for floor
​
def nb_year(p0, percent, aug, p):
    # Take the current population and check if it is already at or above the
    # desired population
    # Then add the changes in a while loop of while p0 is less than p
    # In that loop I will continue to update p0 with the new population until
    # it is at the desired level iterating a counter for the num of years
    
    # Short circuit if p0 is already greater than or eqaul to p
    if p0 >= p:
        return 0
    
    # Set up num_of_years variable to 0
    num_of_years = 0
    
    # While p0 is less than p or while p0 is not greater than or equal to p
    while p0 < p:
        # Something that was found was that percent was give in the number format
        # so it needed to be divided by 100 to get it to the decimal format
        # Need to make sure we round down the population after each run using math.floor
        p0 = math.floor(p0 + (p0 * (percent/100)) + aug)
        # Add one year every iteration
        num_of_years += 1
    
    # Return the total number of years
    return num_of_years
        