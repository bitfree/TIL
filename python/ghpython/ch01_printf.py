from ctypes import *

libc = CDLL("libc.so.6")
message_string = b"Hello world!\n"
libc.printf(b"Testing: %s", message_string)
