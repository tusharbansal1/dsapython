# shoppingList = ['Milk', 'Cheeese', 'Butter']

# access element
# print(shoppingList[2])
# print(shoppingList[-1])
# print('Milk' in shoppingList)


# Traverse list
# for i in range(len(shoppingList)):
#     shoppingList[i] = shoppingList[i] + "+"
#     print(shoppingList[i])


# update/insert
# myList = [1,2,3,4,5,6,7]
# print(myList)
# myList[2] = 33
# print(myList)
# myList.insert(0,111)
# print(myList)
# myList.append(555)
# print(myList)
# newList=['abc','dsd','df']
# myList.extend(newList)
# print(myList)


# Slice/delete
# testList=[1,2,3,4]
# testList[0:2] = ['a','b'] 
# print(testList[0:2])

# testList.pop(1)
# print(testList)
# del testList[0:2]
# testList.remove(1)
# print(testList)


# search
# my_list=[10,20,30,40,50,60,70,80]
# in operator
# target = 50
# if target in my_list:
#     print(f"{target} is in list")
# else:
#     print(f"{target} is not in list")   

# linear search
# def linearSearch(p_list, p_target):
#     for i,value in enumerate(p_list):
#         if value == p_target:
#            return i
#     return -1

# print(linearSearch(my_list,target))


# List operations/functions
a = [1,2,3,4,5,6,7,8]
# b = [4,5,6]
# c = a + b
# print(c)
# a = a * 2
# print(a)

# print(len(a))
# print(max(a))
# print(min(a))
# print(sum(a))
# print(sum(a)/len(a))

# total = 0
# count = 0
# while(True):
#     inp = input("Enter a number: ")
#     if inp == "done":break
#     value = float(inp)
#     total = total + value
#     count = count + 1
#     average = total / count
# print("Average: ",average)    


# myList = list()
# while(True):
#     inp = input("Enter a number: ")
#     if inp == "done":break
#     value = float(inp)
#     myList.append(value)
#     average = sum(myList) / len(myList)
# print("Average: ",average)    

a= 'spam'
b=list(a)
print(b)
c='spam-spam1-spam2'
delimiter = '-'
d=c.split(delimiter)
print(d)

print(delimiter.join(d))
