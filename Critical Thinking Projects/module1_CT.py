import random


# Linear search function
def linear_search(numbers, key):

    for i in range(len(numbers)):
        if numbers[i] == key:
            return i
    return -1


def main():

    # create a 60 element list
    random_array = list(range(1, 61))
    # shuffle the list
    random.shuffle(random_array)
    # input search key
    key = int(input("Enter a number between 1 and 60 to search for: "))
    # result is equal to return value of linear_search()
    result = linear_search(random_array, key)

    if result != -1:
        print('{} was found at index: {}'.format(key, result))
    else:
        print('{} not found in the array'.format(key))


if __name__ == '__main__': main()
