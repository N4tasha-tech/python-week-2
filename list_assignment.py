#Empty
my_list = []

# Appending elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserting
my_list.insert(1, 15)

# Extending
my_list.extend([50, 60, 70])

# Removing 
my_list.pop()

# Sorting it in asc
my_list.sort()

# Print the index of 30
index_of_30 = my_list.index(30)

# Print results
print("Final List:", my_list)
print("Index of 30:", index_of_30)
Final_list = [10, 15, 20, 30, 40, 50, 60]
print("Index of 30:", Final_list.index(30))
