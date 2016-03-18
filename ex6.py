x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "The who know %s and those who %s." % (binary, do_not)

print x
print y

hilarious = False
job_evaluation = "Isn't that joke so funny?! %r"

print job_evaluation % hilarious

job_evaluation2 = "Isn't that joke so funny?! %s"

print job_evaluation2 % hilarious

w = "This is the left side of ..."
e = "a string with a right side/"


print w + e