"""
I would never use this method to retrieve the current username, it is not protable at all.
In windows it works since Python 3, otherwise only on Linux.
"""

import os

print(os.getlogin())
