# In this pattern, we will display a single number on the first row,
# The next two numbers of the second row, And the next three numbers on the third row and so on.
# The count of numbers on each row is equal to the current row number.

rows = 6
for i in range(rows):
    for j in range(i):
        print(i,end=' ')
    print(" ")




