
# GCC is required. # https://gcc.gnu.org/

# python3 main.py Hello_World.txt <output file>


import os, platform, sys
from time import sleep

file_name = "deadfish.txt"

try:
	file_name = sys.argv[1]
except:
	pass

def list_to_str(x):
	res = ""
	for _ in x: res += str(_)
	return res

script = ""
print_mode = "false"
mode = "idso"

with open(file_name, "r") as f:
	content = f.readlines()
	if "ascii" in content[0].lower():
		print_mode = "true"
	if "xkcd" in content[1].lower():
		mode = "xdkc"
	content[0] = ""
	content[1] = ""
	content = list_to_str(content).lower()
	
	for _ in content:
		if _ in mode + ";":
			script += _

print("Compiling....")

with open("default.c", "r") as f:
	default = f.read().replace("SCRIPTHERE", script).replace("LENGTHHERE", str(len(script))).replace("PRINTASCII", print_mode).replace("INCREMENT", mode[0]).replace("DECREMENT", mode[1]).replace("SQUARE", mode[2]).replace("OUTPUT", mode[3])
	with open("out.c", "w") as f:
		f.write(default)

out = "out.a"
if platform.system() == "Windows":
	out = "out.exe"

try:
	out = sys.argv[2]
except:
	pass

command = f"gcc out.c -o {out}"

print(f"\nExecuting: {command}")

os.system(command)

os.remove("out.c")

size = os.path.getsize(out)

print(f"Done output file: {out} [{size} bytes]")
