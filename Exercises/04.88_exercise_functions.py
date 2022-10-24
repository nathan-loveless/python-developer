# Highest Even

def highest_even(li):
    highest = 0

    for num in li:
        if num >= highest and num % 2 == 0:
            highest = num
    return highest


print(highest_even([10, 2, 3, 12, 4, 8, 15, 16, 11]))
