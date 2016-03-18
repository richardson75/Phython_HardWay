from sys import argv # sys is a package, this command says get (unpack) the argv feature

script, name = argv # the argument list input called agrv

print "What is your age?", # comma keeps on the same line
age = int(raw_input("-->")) # you can add other text, need to conver to int

print "Have you had a birthday this year",
bday = raw_input("--> enter y or n?")

print "my name is %s, and I am %d years old" % (name, age)
	
def print_again(name, age): # this is a function that prints
	print "Again, my name is %s, and I am %d years old, " % (name, age),
	
print_again(name, age) # calls the function, passing in vars

def year_born(age,current_year):  # this is a function that returns something
	if bday == "y":
		return current_year-age
	else:
		return current_year-age-1
		
print "I was born in %d" % year_born(age, 2016)nd I am %d years old" % (
	name, age)
