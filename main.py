def sort(numbers):
    if len(numbers) <= 1:
        return numbers
    if numbers[0] > numbers[1]:
        return [numbers[1]] + sort([numbers[0]] + numbers[2:])
    return [numbers[0]] + sort(numbers[1:])


def run_sort(numbers):
    numbers = sort(numbers)
    if is_sort(numbers):
        return numbers
    return run_sort(numbers)


def is_sort(numbers):
    return all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))


if __name__ == '__main__':
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(numbers)
    new_num = run_sort(numbers)
    print(new_num)
