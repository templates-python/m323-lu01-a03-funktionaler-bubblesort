"""Funktionaler Bubblesort.

Aufgabenstellung: https://wiki.bzz.ch/modul/m323/learningunits/lu01/aufgaben/funktionalerbubblesort
"""

def sort(values):
    values = bubble_sort(values)
    if is_sort(values):
        return values
    return sort(values)


def bubble_sort(values):
    if len(values) <= 1:
        return values
    if values[0] > values[1]:
        return [values[1]] + bubble_sort([values[0]] + values[2:])
    return [values[0]] + bubble_sort(values[1:])


def is_sort(values):
    return all(values[i] <= values[i + 1] for i in range(len(values) - 1))


if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    arr_new = sort(arr)
    print(arr_new)
