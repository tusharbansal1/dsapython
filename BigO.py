#O(1)------->
# def multiply_numbers(n):
#     return n*n

# print (multiply_numbers(2))


#O(n)------->
# def print_items(n):
#     for i in range(n):
#      print(i)
#     for j in range(n):
#      print(j) 

# print_items(10)

#O(n*2)--------->
# def print_item(n):
#    for i in range(n):
#       for j in range(n):
#         print(i,j)

# print_item(10)

#O(n*2 + n) ---------> (drop non dominent term +n)
def print_item(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

    for k in range(n):
        print(k) 

print_item(10)