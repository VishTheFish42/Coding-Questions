'''
NEIGHBORING ELEMENTS
Given a two-dimensional array and the position of an element (rows and columns start with 1), return the values of all neighboring elements.
'''

def give_surrounding_elements(arr, r, c):
    num_rows = len(arr)
    if num_rows == 0:
        return []
   
    num_cols = len(arr[0])

    neighbors = []

    for row in [-1, 0, 1]:
        for col in [-1, 0, 1]:
            if row == 0 and col == 0:
                continue

            if 0 <= r + row - 1 < num_rows and 0 <= c + col - 1 < num_cols:
                neighbors.append(arr[r + row - 1][c + col - 1])
    
    return neighbors
