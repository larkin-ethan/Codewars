import numpy
import math
​
def thin_or_fat(matrix):
    # Note this only works if all of the test matrix have the same width and height
    width = 0
    height = 0
    # Transpose the matrix to make the rows become columns
    t_matrix = numpy.transpose(numpy.array(matrix))
    for i in range(len(matrix)):
        # Reset the total height and width of each row every time we go to a new row
        total_width = 0
        total_height = 0
        # Get the index of each element of the inside array
        for j in range(len(matrix[i])):
            # Assume the array is the same height and width you should be able
            # to use the same index for both of them
            total_width += matrix[i][j]
            total_height += t_matrix[i][j]
        # Check if the total width is greater than zero on both width and height
        # and return none if not
        if total_width >= 0:
            width += math.sqrt(total_width)
        else:
            return None
        
        if total_height >= 0:
            height += math.sqrt(total_height)
        else:
            return None
​
    # Compare the width and height to return the correct string
    if width > height:
        return "fat"
    elif width < height:
        return "thin"
    else:
        return "perfect"