
#  Write a Python Program to find largest element in an array OR list .


def find_largest_element(list):
    if not list:
        return "The list is empty:"

    largest_element = list[0]

    for element in list:
        if element > largest_element :
            largest_element = element

    return largest_element


my_list = [23,32,54,44,65,59,90,55,63,14,51,99]

result = find_largest_element(my_list)
print(f"The largest element in the list is: {result}")


