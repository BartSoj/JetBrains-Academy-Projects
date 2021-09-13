def range_sum(numbers, start, end):
    numbers = [num for num in numbers if start <= num <= end]
    res = 0
    for num in numbers:
        res += num
    return res


input_numbers = [int(num) for num in input().split()]
a, b = [int(num) for num in input().split()]
print(range_sum(input_numbers, a, b))
