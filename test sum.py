from random import randint
from sum import*

def test_code():
	for i in range(1000):
		m=randint(-1000, 1000)
		n=randint(-1000, 1000)
		assert(get_sum(m, n)==m+n)