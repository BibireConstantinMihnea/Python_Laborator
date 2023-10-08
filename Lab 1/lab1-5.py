matrix = [['f', 'i', 'r', 's'],
          ['n', '_', 'l', 't'],
          ['o', 'b', 'a', '_'],
          ['h', 't', 'y', 'p']]
rows = len(matrix)
cols = len(matrix[0])
row_start = 0
col_start = 0

while(row_start < rows and col_start < cols):
    for i in range(col_start, cols):
        print(matrix[row_start][i], end='')
    
    row_start += 1

    for i in range(row_start, rows):
        print(matrix[i][cols - 1], end='')
    
    cols -= 1

    if(row_start < rows):
        for i in range(cols - 1, col_start - 1, -1):
            print(matrix[rows - 1][i], end='')
    
    rows -= 1
    
    if(col_start < cols):
        for i in range(rows - 1, row_start - 1, -1):
            print(matrix[i][col_start], end='')
    
    col_start += 1