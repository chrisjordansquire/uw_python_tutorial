#Run this script with nosetests (probably in /usr/local/bin)

#Can't import with import statement because module names
#start with a number
gen = __import__('07_generators')

#Many more useful things are in nose.tools. See the docs.
from nose.tools import raises

#simple tests

def test_trivial():
	pass

def test_fail():
	assert(1==0)

@raises(KeyError)
def test_exception():
	d = {}
	d[1]

def test_exception_error():
	d={}
	d[1]

def test_primeGenerator():
	pGen = gen.primeGenerator()
	true = [3,5,7,11,13,17,19,23]
	actual = []
	for i in xrange(len(true)):
		actual.append(pGen.next())
	assert( true == actual )
