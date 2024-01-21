
# Writing to a file

a = "Pragati is a good girl"
#
# with open("file.txt", "w") as f:
#     f.write(a)
"""
fp = open("file.txt", "w")
fp.write(a)
fp.close()
"""

# Reading a file
with open("file.txt", 'r') as fi:
    str1 = fi.read()
    print(str1)

# Append to a file

with open('file.txt', 'a') as f:
    f.write(" and Kaustubh is a good boy")