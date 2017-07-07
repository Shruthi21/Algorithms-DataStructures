integer = int(raw_input( ))
if integer <= 10 and integer >= 0:
	character = raw_input( )
	if len(character) <= 15 and len(character) >= 1:
		print (integer * 2)
		print character
	else:
		print 'INVALID INPUT'
else:
	print 'INVALID INPUT'

