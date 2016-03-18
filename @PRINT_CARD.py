from sys import argv # sys is a package, this command says get (unpack) the argv feature

script, name = argv # the argument list input called agrv

print "What is your age?", # comma keeps on the same line
age = int(raw_input("-->")) # you can add other text, need to conver to int

print "my name is %s, and I am %d years old" % (
	name, age)