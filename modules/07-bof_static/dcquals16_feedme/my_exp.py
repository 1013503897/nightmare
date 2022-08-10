from pwn import *

target = process('./feedme')


target.interactive()