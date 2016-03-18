# sys is a package, this command says get (unpack) the argv feature from the package
# this command unpacks argv, which is the input being passed to this script
from sys import argv 

#This describes the argumentlist input called agrv and it also assigns the VARIABLES based on what is passed
script, filename = argv

#open() is python a FUNCTION, it's how you open a file
#the open function returns the file object
txt = open(filename)

#Here we call the read() function w/o passing it anything 
print "Here's your file %r:" % filename
print txt.read()

#This takes the input from the raw_input() function and puts into a var
#this is similar to how we got the filenam var above
print "Type the name of the file again:"
file_again = raw_input(":> ")

#now we call the open function
txt_again = open(file_again) 

#and we call the read function
print txt_again.read()

print "hi"

# looks like you cannot do this
x = txt_again.read()
print x


