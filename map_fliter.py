my_list = [1,2,3,4,5,6,7,8,9,10]
my_list1 = [1,2,3,4,5,6,7,8,9,10]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))
new_list1 = list(map(lambda x: (x%2 == 0) , my_list1))

print(new_list)
print(new_list1)


#Nested Loops in List Comprehension
transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]
# how many element in each item of list:4 times 
for i in range(len(matrix[0])):
    #initiative the row list  
    transposed_row = []
    # loop 2 times
    for row in matrix:
        #row is variable 
        transposed_row.append(row[i])
    # append it to final list
    transposed.append(transposed_row)
print(transposed)

#Transpose of a Matrix using List Comprehension
matrix1 = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix1] for i in range(2)]
print (transpose)

# random list
randomList = [1, 'a', 0, False, True, '0']
filteredList = filter(None, randomList)
print('The filtered elements are:')
for element in filteredList:
    print(element)
