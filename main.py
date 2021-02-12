def main():
    arr1 = [1, 2, 3, 4, 5, 6, 7]
    arr2 = [2, 4, 7]
    print(task1(arr1, arr2))

    arr3 = [2, 3, 5, 0, 7, 0, 6, 3, 0, 1]
    arr3 = task2(arr3)
    print(arr3)

def task1(arr1, arr2):
    return list(filter(lambda x: x not in arr2, arr1))


def task2(arr1):
    return list(filter(lambda x: x != 0, arr1))


if __name__ == '__main__':
    main()
