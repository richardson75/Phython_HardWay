print "I \"understand\" joe"

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list
\t* catfood
\t* fishies
\t* Catnip\n\t* Grass
"""

fat_cat2 = '''
I'll do a list
\t* catfood
\t* fishies
\t* Catnip\n\t* Grass
"""
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print fat_cat2

print "the \b tabby cat \"says\" %s" % tabby_cat

print "the tabby cat \"says\" %r" % tabby_cat