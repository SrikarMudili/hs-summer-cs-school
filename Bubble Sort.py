def sort(numbers):
    for i in range(len(numbers)-1, 0, -1):
        for j in range(i):
            if numbers[j]>numbers[j+1]:
                temporary = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temporary


numbers = [5, 3, 8, 6, 7, 2]
sort(numbers)
print(numbers)