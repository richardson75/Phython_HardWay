# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#dont need to use the *args

def print_two_again(arg3, arg4):
	print "arg3: %r, arg4: %r" % (arg3,arg4)
	
def print_one(arg1):
	print "arg1: %r" % arg1

def print_none():
	print "I got nothing"

print_two("Zed", "Shaw")
print_two_again("Chris", "Richardson")
print_one("test")
print_none()

