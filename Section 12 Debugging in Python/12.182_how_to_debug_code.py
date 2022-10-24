# Debugging in Python

# tips
# 1. Linting - allows us to detect, as we code, issues with our code
# num is already underlined red, even though we didn't run it yet
# num + 4

# 2. Always use IDE (PyCharm) or an editor like VS Code
# 3. Learn to read errors

# pdb - Python Debugger (it is built-in to python)
import pdb

import pdb


def add(num1, num2):
    pdb.set_trace()
    t = 4 * 5
    return num1 + num2


print(add(1, 5))
