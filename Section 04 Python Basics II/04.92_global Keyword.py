# Global Keyword
# Global says, use the global 'total' if it exists
total = 0


def count(total):
    total += 1
    return total


print(count(count(count(total))))
