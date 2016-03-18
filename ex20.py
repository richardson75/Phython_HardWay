from sys import argv

script, input_file = argv

# defines a function that prints a file after reading it
def print_all(f):
	print f.read()

#defines a function the moves to the start of a file
def rewind(f):
	f.seek(0)
	
#function the prints the current line of file	
def print_a_line(line_count, f):
	print line_count, f.readline()

#opens the file that was passed
current_file = open(input_file)

print "First lest print the whole file:\n"

print_all(current_file)

print "now let rewind like a type"

rewind(current_file)

#not sure how to get the line number
fileline = current_file.readline()
print "we are currently line: %s \n" % (fileline)

pos = current_file.tell()
print "we are currently at: %d \n" % (pos)

print "lets print three lines"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
