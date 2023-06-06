def find_duplicate_element(lst):
    seen = set()
    for element in lst:
        if element in seen:
            return element
        else:
            seen.add(element)
    return None


def create_transpose(matrix):
    original_height = len(matrix)
    if not original_height:
        return []
    original_width = len(matrix[0])
    if not original_width:
        return []
    transpose = [None] * original_width
    for i in range(original_width):
        transpose[i] = [None] * original_height
    for i in range(original_width):
        for j in range(original_height):
            transpose[i][j] = matrix[j][i]
    return transpose


def propagate_zeros(matrix):
    height = len(matrix)
    if not height:
        return matrix
    width = len(matrix[0])
    if not width:
        return matrix
    zeroed_columns = set()
    zeroed_rows = set()
    for i in range(height):
        for j in range(width):
            if matrix[i][j] == 0:
                zeroed_columns.add(i)
                zeroed_rows.add(j)
    for i in range(height):
        for j in range(width):
            if i in zeroed_columns or j in zeroed_rows:
                matrix[i][j] = 0
    return matrix

# find_duplicate_element example
# print(find_duplicate_element([1,2,3,4,5,4,5,6]))

# create_transpose example
# print(create_transpose([[1, 2, 3], [4, 5, 6]]))

# propagate_zeros example
matrix = [
    [0, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]
print(propagate_zeros(matrix))

