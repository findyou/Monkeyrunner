# conding =utf8
import sys
print(sys.argv)
print(sys.path[0])
print(sys.argv[0])

str = sys.path[0]
index = str.rfind(':')
newstr = str[index-1:]
print(newstr)
newstr.replace('\\','/')
print(newstr)