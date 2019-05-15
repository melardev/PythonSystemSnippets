import getpass
import os

username = getpass.getuser()
print('Your username is %s' % username)

# Does not trigger any Error if key name was not found
print(os.environ.get('USERNAME'))
print(os.environ['USERNAME'])  # triggers KeyError exception if not found

# Returns second arg as value if key name was not found
print(os.environ.get('MOST_LIKELY_NON_EXISTING', 'Default value if not found'))
