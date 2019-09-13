from random import randint
from sum import*

def test_code():
	for i in range(1000):
		m=randint(-100000, 100000)/100
		n=randint(-100000, 100000)/100
		assert(get_sum(m, n)==m+n)