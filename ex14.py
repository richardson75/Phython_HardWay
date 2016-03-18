from sys import argv

script, user_name, food = argv
prompt2 = '>>>> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s" % user_name
likes = raw_input(prompt2)

print "Where do you live %s?" % user_name
lives = raw_input(prompt2)

print "What kind of computer do you have?"
computer = raw_input(prompt2) 

print """
Alright, so you said %r about liking me.
You like in %r. Not sure where that is.
And you have a %r computer. nice.
You also like %r
""" % (likes, lives, computer, food) 