def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n):
        for j in range(0, n - i - 1):

            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers


def selection_sort(numbers):
    n = len(numbers)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j

        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    return numbers


data = [64, 34, 25, 12, 22, 11, 90]

print("Original List:", data)

print("Bubble Sort:", bubble_sort(data.copy()))
print("Selection Sort:", selection_sort(data.copy()))
