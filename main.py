def sort(list):
    list = bubble_sort(list)
    if is_sort(list):
        return list
    return sort(list)


def bubble_sort(list):
    if len(list) <= 1:
        return list
    if list[0] > list[1]:
        return [list[1]] + bubble_sort([list[0]] + list[2:])
    return [list[0]] + bubble_sort(list[1:])


def is_sort(list):
    return all(list[i] <= list[i + 1] for i in range(len(list) - 1))


if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    arr_new = sort(arr)
    print(arr_new)
