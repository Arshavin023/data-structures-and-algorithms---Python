import random 


def linear_search(numbers_list, number_to_find):
    answer = None
    for index,number in enumerate(numbers_list):
        if number == number_to_find:
            return index
        return -1

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
        



if __name__ == '__main__':
    numbers_list = sorted(set([random.randint(1,100) for _ in range(1,100)]))
    print(numbers_list)
    number_to_find = int(input('enter number to find: '))
    # print(f"Number found at index {linear_search(numbers_list, number_to_find)} using linear search")
    print(f"Number found at index {binary_search(numbers_list, number_to_find)} using linear search")
    
