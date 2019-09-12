import one

print("top level in two.py")

one.func()

if __name__ == "__main":
	print("two.py is being run directly")
else:
	print("two.py is being imported into another module")