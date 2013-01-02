"""
Short intro to loops and control flow in python
"""

#Loops

#for loops
for i in range(3):
	print "Meow"

x = [i**2 for i in range(3)]

#Can iterate over an iterable
for i in x:
	print i

#Build a non-trivial, non-list iterable
keys = [1992+i*4 for i in range(6)]
values = []
for prez in ['Clinton', 'Bush', 'Obama']:
	values.extend([prez]*2)

winners = dict(zip(keys, values))

#iterate over non-trivial, non-list iterable
for year, prez in winners.items():
	print "Congradulations, " + prez + " won in " + year


#There are also while loops
count=0
while count<3:
	count += 1
	print count

s = "a pine tree"

if s is "a tree":
	print "kinda true"
elif s is "a pine":
	print "sorta true"
else:
	print "just not true"

#there are also continue/break statements for the loops

for i in range(20):
	if not i%2:
		continue
	elif not i%19:
		break
	else:
		print i
