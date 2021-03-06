from subprocess import call
import offsetgen
import kcachedecryptor as kcachedec
import kcachedownloader as kcachedown
import offsetgrabber as grab
import sys
import os
import platform

if __name__ == "__main__":
	if len(sys.argv) > 1:
		if sys.argv[1] == "kernelgen":
			device = sys.argv[2]
			build = sys.argv[3]
			kcachedown.download(device, build)
			kcachedec.decrypt(device, build)
			platform1 = platform.platform()
			if platform1 == "linux" or platform1 == "linux2" or platform1 == "darwin":
				print("Copy this line to paste into untether.json")
				call("strings kernelcache.bin | grep 'Darwin Kernel >> Darwin.txt'")
			else:
				is32bit = (platform.architecture()[0] == '32bit')
				system32 = os.path.join(os.environ['SystemRoot'], 'SysNative' if is32bit else 'System32')
				bash = os.path.join(system32, 'bash.exe')
	
				bashexec = "strings kernelcache.bin | grep 'Darwin Kernel'"
				print("Copy this line to paste into untether.json")
				call(bash + " -c '" + bashexec + " >> Darwin.txt'")
			print("Offsets needed for doing stuff (Clock_ops is the 5th one)")
			print("ios version?")
			ios = input()
			print(grab.Offsets(device, ios))
		elif sys.argv[1] == "offsetgen":
			with open(sys.argv[2]) as f:
				offsets = f.read().rstrip().split('\n')
				print(offsetgen.GenerateOffsetList(offsets))
		else:
			print("Usage:\npy kcachify.py kernelgen iPad2,1 13F69\npy kcachify.py offsetgen offsets.txt")
	else:
		print("Usage:\npy kcachify.py kernelgen iPad2,1 13F69\npy kcachify.py offsetgen offsets.txt")