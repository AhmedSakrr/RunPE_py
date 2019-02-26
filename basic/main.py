from run_pe import show_buf, run_portable_executable


content = b""
with open("winmine.exe", "rb") as f:
    byte = f.read(1)
    while byte != b"":
        content += byte
        byte = f.read(1)

content = bytearray(content)
content[0x2afb] = 0x30
content[0x2afc] = 0x81
content = bytes(content)

print(run_portable_executable(content))