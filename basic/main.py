from run_pe import show_buf, run_portable_executable


content = b""
with open("D:\\self\\program\\c++\\a\\wrapper\\winmine.exe", "rb") as f:
    byte = f.read(1)
    while byte != b"":
        content += byte
        byte = f.read(1)

print(run_portable_executable(str(content)))