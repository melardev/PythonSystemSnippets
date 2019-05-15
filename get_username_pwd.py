import pwd
import os

print(pwd.getpwuid(os.geteuid()).pw_name)
print(pwd.getpwuid(os.geteuid())[0])
