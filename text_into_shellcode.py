def shellcodecreator():
	inp = raw_input("Enter the payload to convert into bytes here: ")
	shellcode = "".join(["\\x%02x" % ord(i) for i in inp])
	print shellcode

shellcodecreator()
