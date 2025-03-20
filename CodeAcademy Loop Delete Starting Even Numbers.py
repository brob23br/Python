'''Write a function called delete_starting_evens() that has a parameter named my_list.

The function should remove elements from the front of my_list until the front of the list is not even. The function should then return my_list.

For example if my_list started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(my_list) should return [11, 12, 15].

Make sure your function works even if every element in the list is even!'''

'''hint: Use a while loop to check two things. First, check if the list has at least one element, using len(my_list). 
Second, check to see if the first element is odd using mod (%). If both of those are True, slice off the first element of the list using my_list = my_list[1:].'''

def delete_starting_evens(my_list):
    while len(my_list) > 0 and my_list[0] % 2 == 0:
        my_list = my_list[1:]
    return my_list

# Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))