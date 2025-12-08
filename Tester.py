msg = "Roll a dice"
print(msg + " (fake roll)")
print(3+3)

"""Let's build upon the previous example by using packages.

In Python, packages are how you obtain any number of useful code libraries, 
typically from PyPI, that provide additional functionality to your program. 
For this example, you use the numpy package to generate a random number.
"""

import numpy as np

msg = "Roll a dice"
print(msg)

print(np.random.randint(5,9))