# binary strings are prefixed with a b

chars_as_bytes = b"single-byte string"
print(chars_as_bytes)

# to print as a unicode string the byte-string must be decoded
print(chars_as_bytes.decode())

# to turn a unicode string into a byte-string, use encode
# unicode string to byte-string is encode
# byte-string to unicode is decode

my_byte_string = "some unicode string".encode()
print(my_byte_string)
