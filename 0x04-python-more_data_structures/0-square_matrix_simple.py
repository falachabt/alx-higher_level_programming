#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Check if the matrix is empty
    if not matrix:
        return None
    # Create a new matrix with the squared values using a nested list comprehension
    squared_matrix = [[i**2 for i in row] for row in matrix]
    # Return the new matrix
    return squared_matrix
            