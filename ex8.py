formatter = "%r %r %r %r"

print formatter % (1 ,2, 3, 4)
print formatter % ('one', 'two', 'three', 'four')
print formatter % (True, False, False, True)
print formatter % (formatter, formatter,formatter,formatter)
print formatter % (
	"I had this thing.",
	"That your could type up right.'",
	"but it didn't sing",
	"so I said goodnight."
)

i= 2 + 2
print formatter % ('one', 'two', 'three', i)