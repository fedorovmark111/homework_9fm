from random import randint
from sum import*

def test_code():
	for i in range(1000):
		m=randint(-1000, 1000)/10
		n=randint(-1000, 1000)/10
		assert(get_sum(str(m), str(n))==str(m)+str\(n))