people = 30
cars = 40
buses = 15
if 1:
	print "We sholud take the cars."
elif 1:
	print "We should not take the cars."
else:
	print "We can't decide."
#Python 只会运行它碰到的是 True 的第一个区块，所以只有第一个为 True 的区块会被运行。


if cars > people:
	print "We sholud take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."
	
if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."
	
