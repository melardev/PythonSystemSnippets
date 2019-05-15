"""
This demo shows how to retrieve the username using expanduser function.
This is not my ideal form of getting the username, I have other demos for that, the good point
is that this is really portable code
"""
import os

# Get the home directory path like C:/Users/melardev
home_directory = os.path.expanduser('~')

print("User's home Directory: %s" % home_directory)

# Get last bit of the path, it should contain the username
print("username: %s" % os.path.split(home_directory)[-1])
