# Useful Modules 2
import datetime
from array import array

# datetime
print(datetime.time(5, 45, 2))
print(datetime.date.today())

# array
# A little different from lists in Python, they are dynamic. They take up less memory and are faster
arr = array('i', [1, 2, 3])
print(arr)
