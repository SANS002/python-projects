
lent_of_elements =int(input("Enter the lenth of elements:"))

list1=[input("enter the element:") for i in range(lent_of_elements)]

find_value = input("enter the value to find :")

def linear_search(arr,target):
    for index,element in enumerate(arr):
        if element==target:
            return index
    return -1

print(linear_search(list1,find_value))


