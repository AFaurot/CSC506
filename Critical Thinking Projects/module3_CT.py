import random
import time

# merge function inspired from CSC506 Zybook chapter 3
def merge(numbers, i, j, k):
    size = k - i + 1
    merged_list = [0] * size

    merge_pos = 0
    left_pos = i
    right_pos = j + 1

    while left_pos <=j and right_pos <=k:
        if numbers[left_pos] <= numbers[right_pos]:
            merged_list[merge_pos] = numbers[left_pos]
            left_pos += 1
        else:
            merged_list[merge_pos] = numbers[right_pos]
            right_pos += 1
        merge_pos = merge_pos + 1

    while left_pos <= j:
          merged_list[merge_pos] = numbers[left_pos]
          left_pos += 1
          merge_pos += 1

    while right_pos <= k:
        merged_list[merge_pos] = numbers[right_pos]
        right_pos = right_pos + 1
        merge_pos = merge_pos + 1

    for merge_pos in range (size):
        numbers[i + merge_pos] = merged_list[merge_pos]

# Merge sort function inspired from CSC506 Zybooks chapter 3
def merge_sort(numbers, i, k):
    j = 0
    if i < k:
        j = (i + k) // 2

        merge_sort(numbers, i, j)
        merge_sort(numbers, j + 1, k)

        merge(numbers, i, j, k)

# Simple implementation of Bubble sort
def bubble_sort(numbers):

    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(0, len(numbers) -1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                is_sorted = False
    return numbers


def main():

    # numbers array
    numbers = []
    # List size to allow user input for how large of a list to sort
    list_size =int(input("Enter an integer value for list size:"))
    # If the list is less than 100, append a random number between 0 and 100
    if list_size <= 100:
        for i in range(list_size):
            numbers.append(random.randint(0, 100))
    # If list is between 100 and 20,000 append between 0 and list_size
    elif 100 < list_size <= 20000:
        for i in range(list_size):
            numbers.append(random.randint(0, list_size))
    # If list is between 20,000 and 50,000 Warn that it might take a while and continue anyway
    elif 20000 < list_size <= 50000:
        print("!!WARNING!! This list is very large and bubble sort might take a very long time")
        choice = input("Continue, Y/N? : ")
        if choice == "n" or choice == "N":
            quit()
        elif choice == "y" or choice == "Y":
            for i in range(list_size):
                numbers.append(random.randint(0, list_size))
        else :
            print("Invalid input")
    # If list is larger than 50,000 only perform merge sort
    else:
        print(f"The list of {list_size} elements is to large for bubble sort only using merge sort")
        for i in range(list_size):
            numbers.append(random.randint(0, list_size))
    # Copy of numbers array
    numbers2 = list(numbers)
    if list_size <= 100:
        print("UNSORTED:", numbers)
    else:
        print("UNSORTED LAST 100:", numbers[-100:])
    # Record execution start time
    m_start_time = time.perf_counter()
    # Execute merge sort
    merge_sort(numbers, 0, len(numbers) - 1)
    # Record execution end time and compute end - start for execution time in seconds
    m_end_time = time.perf_counter()
    m_execution_time = m_end_time - m_start_time
    if list_size <= 100:
        print('SORTED WITH MERGE SORT', numbers)
    else:
        print('MERGE SORT LAST 100', numbers[-100:])

    if list_size <= 50000:
        b_start_time = time.perf_counter()
        bubble_sort(numbers2)
        b_end_time = time.perf_counter()
        b_execution_time = b_end_time - b_start_time
        if list_size <= 100:
            print('SORTED WITH BUBBLE SORT:', numbers2)
        else:
            print('BUBBLE SORT LAST 100', numbers2[-100:])
        print(f"Bubble sort took : {b_execution_time} seconds")
    print(f"Merge sort took : {m_execution_time} seconds")

if __name__ == '__main__': main()