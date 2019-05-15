"""
Three different ways of retrieving the pc name.
My preferred way is to use gethostname() which I think it is more widely supported by any platform
"""

import os
import platform
import socket

pc_name1 = platform.node()
pc_name2 = socket.gethostname()
pc_name3 = os.environ["COMPUTERNAME"]

print(pc_name1)
print(pc_name2)
print(pc_name3)
