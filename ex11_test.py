print '\nWhat\'s your name ?' 
name = raw_input('--> ')
print '\nHow old are you, %s?' % name,
age = int(raw_input('xx')) # you can put anything in here
print '\nHow tall are you (in cms), %s?' % name,
height = int(raw_input())
print '\nHow much do you weigh (in kgs), %s?' % name,
weight = int(raw_input())

print '\nSo, %s is %d years old, %d cms tall and weighs %d kgs.\n' %(
name, age, height, weight)

#another example
print "Halt!"
s = raw_input("Who Goes there? ")
print "You may pass,", s # this is a simple way to add the strings, only works at the end.

#another example
print "Halt2!"
name2 = raw_input("Who Goes there? ")
print 'You may pass, %s' % name2