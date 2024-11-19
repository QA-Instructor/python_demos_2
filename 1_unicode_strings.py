# unicode examples
print('#' * 90)
# use \u for a unicode character
euro = "\u20ac"
print(euro + str(5.99))

copyright = "\u00A9"
print(copyright)

# use \N{} for a named unicode character
print("\N{euro sign}")

# print examples
print('#' * 90)
print('one', end="---")
print('two')
print('three')
print('four', 'five', 'six', sep='\t')
print('seven')

firstname = 'Julie'
lastname = 'Dooley'

# concatenation
fullname = firstname + ' ' + lastname
print(fullname)
# the print function uses a space as the default separator
print(firstname, lastname)

alist = ['one', 'two', 'three']

s = ""
for item in alist:
    s = s + item + ' '

print(s)
