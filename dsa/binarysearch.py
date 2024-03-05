import random
import time 

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ +"took " + str((end-start)*1000) + " mil sec")
        return result
    return wrapper


@time_it
def linear_search(numbers_list, number_to_find):
    for index, number in enumerate(numbers_list):
        if number == number_to_find:
            return index
    return -1

@time_it
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0 

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]
        
        if mid_number == number_to_find:
            return mid_index
        
        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

@time_it
def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1
    mid_index = mid_index = (left_index + right_index) // 2

    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1
    
    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1 
    else:
        right_index = mid_index + 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

@time_it
def find_all_occurances(numbers, number_to_find):
    index = binary_search(numbers, number_to_find)
    indices = [index]
    # find indices on left hand side
    i = index-1
    while i >=0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i<len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)

if __name__ == '__main__':
    # numbers_list = sorted(set([random.randint(1,100) for _ in range(1,10**4)]))
    numbers_list = [1,4,6,11,15,15,15,17,21,34,34,56]
    left_index = 0
    right_index = len(numbers_list) - 1
    print(numbers_list)
    # number_to_find = int(input('enter number to find: '))
    # index = binary_search_recursive(numbers_list, 15, left_index, right_index)
    index = find_all_occurances(numbers_list,15)
    # print(f"Number found at index {linear_search(numbers_list, number_to_find)} using linear search")
    print(f"Number found at index {index} using binary recursive search")
