from pathlib import Path


# ABSOLUTE PATH METHOD (--> Path started from root of hard disks)
# Example No.01: c:\Program Files\Microsoft

# RELATIVE PATH METHOD (--> Path started within current directory)

# To check if path exist:
path = Path("ecommerce")
print(path.exists())
# Note that returns boolean value.
# The example code above is TRUE.

# The example code below is FALSE, since "madara" directory does not exist.
path = Path("madara")
print(path.exists())

# But we can make directory if there is none exists.
# Example:
#path = Path("emails")
#print(path.mkdir())

# Also to remove directory:
# (Disabled in order to see 'email' directory in ecommerce)
#path = Path("emails")
#print(path.rmdir())

# If code above was enabled, you will not see 'email' directory
# since right after created by path.mkdir, the said directory was then
# deleted immediately.

# Code below is used to search FILES ONLY in the said directory:
path = Path('ecommerce')
for file in path.glob('*.*'):
    print(file)
# Note that the first asterisk symbol '*' is used to search all
# FILE NAME while the second asterisk is for the FILE TYPE.

# You can search FILE TYPE regardless of FILE NAME.
# Example: '*.xls', '*.py', '*.ppt'
# Likewise can also search all FILE NAME regardless of FILE TYPE.
# Example: 'a.*', 'research.*', 'cmd.*'