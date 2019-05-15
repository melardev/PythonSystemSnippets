"""
How to check if we are on windows using this trick, I don't like it much but
it is here just for completeness. I prefer other methods, also shown in this snippets repository
"""
import sys

is_windows = hasattr(sys, 'getwindowsversion')
print('is this a windows system? %s' % is_windows)
