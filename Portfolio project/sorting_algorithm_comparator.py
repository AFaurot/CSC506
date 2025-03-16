import random
import time

# Partition function utilized by quick_sort(). inspired from CSC 506 Zybooks chapter 3
def partition(numbers, start_index, end_index):
    # Midpoint value is pivot
    midpoint = start_index + (end_index - start_index) // 2
    # Select the value at midpoint as the pivot for comparisons
    pivot = numbers[midpoint]

    # Low and high are used
    low = start_index
    high = end_index

    is_partitioned = False
    while not is_partitioned:

        # Increment low index while values at numbers[low] < pivot
        while numbers[low] < pivot:
            low = low + 1

        # Similar logic to decrement high index
        while pivot < numbers[high]:
            high = high - 1

        # If low and high have crossed partitioning loop is complete.
        if low >= high:
            is_partitioned = True
        # Else swap elements and increment low and decrement high
        else:
            temp = numbers[low]
            numbers[low] = numbers[high]
            numbers[high] = temp
            low = low + 1
            high = high - 1
    # return last index of left segment
    return high


# quick sort based on CSC 506 Zybooks chapter 3
def quick_sort(numbers, start_index, end_index):

    if end_index <= start_index:
        return

    # high = end index of left segment in partition function - see return value
    high = partition(numbers, start_index, end_index)

    # Recursion to sort left side
    quick_sort(numbers, start_index, high)

    # Recursion to sort right side
    quick_sort(numbers, high + 1, end_index)


# Insertion sort
def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        j = i

        # function to swap position of numbers when right is smaller than left
        while j > 0 and (numbers[j] < numbers[j-1]):
            temp = numbers[j]
            numbers[j] = numbers[j-1]
            numbers[j-1] = temp
            j -= 1


# merge function inspired from CSC506 Zybook chapter 3
def merge(numbers, i, j, k):
    # Size of the partition
    size = k - i + 1
    # Temporary array
    merged_list = [0] * size
    # Merged index
    merge_pos = 0
    # Left position
    left_pos = i
    # Right position
    right_pos = j + 1

    # Add the smallest number from left or right to the merged list
    while left_pos <= j and right_pos <= k:
        if numbers[left_pos] <= numbers[right_pos]:
            merged_list[merge_pos] = numbers[left_pos]
            left_pos += 1
        else:
            merged_list[merge_pos] = numbers[right_pos]
            right_pos += 1
        merge_pos = merge_pos + 1

    # Continue while left position is less than midpoint
    while left_pos <= j:
        merged_list[merge_pos] = numbers[left_pos]
        left_pos += 1
        merge_pos += 1
    # Continue while right position is less than end index
    while right_pos <= k:
        merged_list[merge_pos] = numbers[right_pos]
        right_pos = right_pos + 1
        merge_pos = merge_pos + 1

    # Copy the temporary array back to the original array
    for merge_pos in range(size):
        numbers[i + merge_pos] = merged_list[merge_pos]


# Merge sort function inspired from CSC506 Zybooks chapter 3
def merge_sort(numbers, i, k):
    j = 0
    if i < k:
        j = (i + k) // 2

        # Recursive sort left and right until one element each
        merge_sort(numbers, i, j)
        merge_sort(numbers, j + 1, k)
        # Call merge() to Merge numbers back in order
        merge(numbers, i, j, k)


# Simple implementation of Bubble sort
def bubble_sort(numbers):

    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(0, len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                is_sorted = False
    return numbers


def main():

    # numbers array
    numbers = []
    # List size to allow user input for how large of a list to sort
    list_size = int(input("Enter an integer value for list size:"))
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
        else:
            print("Invalid input")
    # If list is larger than 50,000 only perform merge sort
    else:
        print(f"The list of {list_size} elements is to large for bubble and insertion sort."
              f" Continuing execution with merge and quick sort")
        for i in range(list_size):
            numbers.append(random.randint(0, list_size))
    # Copy of numbers array
    numbers2 = list(numbers)  # Used by bubble sort
    numbers3 = list(numbers)  # Used by insertion sort
    numbers4 = list(numbers)  # Used by quick sort
    if list_size <= 100:
        print("UNSORTED:", numbers)
    else:
        print("UNSORTED LAST 100:", numbers[-100:])
    # Record merge sort execution start time
    m_start_time = time.perf_counter()
    # Execute merge sort
    merge_sort(numbers, 0, len(numbers) - 1)
    # Record execution end time and compute end - start for execution time in seconds
    m_end_time = time.perf_counter()
    m_execution_time = m_end_time - m_start_time

    # Record quick sort execution start time
    q_start_time = time.perf_counter()
    # Execute quick sort
    quick_sort(numbers4, 0, len(numbers) - 1)
    # Record quick sort execution end time
    q_end_time = time.perf_counter()
    q_execution_time = q_end_time - q_start_time

    if list_size <= 100:
        print('SORTED WITH MERGE SORT', numbers)
        print('SORTED WITH QUICK SORT', numbers4)
    else:
        print('MERGE SORT LAST 100:', numbers[-100:])
        print('QUICK SORT LAST 100:', numbers4[-100:])

    if list_size <= 50000:

        # Call to insertion sort and tracking of execution time
        i_start_time = time.perf_counter()
        insertion_sort(numbers3)  # Execute insertion sort
        i_end_time = time.perf_counter()
        i_execution_time = i_end_time - i_start_time

        # Call to bubble sort and tracking of execution time
        b_start_time = time.perf_counter()
        bubble_sort(numbers2)  # Execute bubble sort
        b_end_time = time.perf_counter()
        b_execution_time = b_end_time - b_start_time

        if list_size <= 100:
            print('SORTED WITH INSERTION SORT:', numbers3)
            print('SORTED WITH BUBBLE SORT:', numbers2)
        else:
            print('INSERTION SORT LAST 100:', numbers3[-100:])
            print('BUBBLE SORT LAST 100:', numbers2[-100:])
        print(f"Insertion sort took : {i_execution_time} seconds")
        print(f"Bubble sort took : {b_execution_time} seconds")
    print(f"Merge sort took : {m_execution_time} seconds")
    print(f"Quick sort took : {q_execution_time} seconds")


if __name__ == '__main__':
    main()
