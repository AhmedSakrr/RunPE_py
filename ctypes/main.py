from ctypes import *


m = cdll.LoadLibrary("RunPE.dll")

content = b""
with open("winmine.exe", "rb") as f:
    byte = f.read(1)
    while byte != b"":
        content += byte
        byte = f.read(1)

content = bytearray(content)
content[0x2afb] = 0x30
content[0x2afc] = 0x81
print(m._Z21RunPortableExecutablePv(bytes(content)))