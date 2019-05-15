import os

# We can use [] operator, .get() or os.getenv()
temp_directory = os.environ['TMP']
print(temp_directory)

temp_directory = os.environ.get('TMP', os.path.expanduser('~/'))
print(temp_directory)

print('I will create a file either in $TMP env variable if it exists, if it does not, then I would create it'
      ' on the current user\'s home directory')
temp_directory = os.environ.get('TEMP_Typo', os.path.expanduser('~/'))
print('I would create the file in %s' % temp_directory)

# os.getenv is deprecated, prefer os.environ[] or os.environ.get()
print(os.getenv('TMP'))
