import os

for i in range(4096):
    os.system(f'wget https://vfsync.org/u/os/buildroot-riscv64/files/0000000000001{hex(i)[2:].zfill(3)}')