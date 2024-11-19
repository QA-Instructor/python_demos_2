# this is an example row from a linux /etc/passwd file
# username:password:userID:GroupID:Comment:home_directory:command_shell

line = 'root::0:0:superuser:/root:/bin/sh'
elements = line.split(':')

print(elements)

elements[0] = 'avatar'
elements[4] = 'The super-user (zero)'

print(elements)

line = ':'.join(elements)
print(line)

