from mymatrix import MyMatrix
a=[[2, 2], [1, 1], [0, 4]]
b=[[3, 2], [5, 4], [0, 5]]
c=[]
def test___add__():
    m1 = MyMatrix(a)
    m2 = MyMatrix(b)
    summ = m1 + m2
    assert(summ.get_data() == [[5, 4], [6, 5], [0, 9]])
    assert(m1.get_data()== a)
    assert (m2.get_data() == b)

def test___sub__():
    m2 = MyMatrix(a)
    m1 = MyMatrix(b)
    subm = m2 - m1
    assert(subm.get_data() == [[-1, 0], [-4, -3], [0, -1]])
    assert (m1.get_data() == b)
    assert (m2.get_data() == a)

def test___newadd__():
    m1 = MyMatrix(a)
    m2 = MyMatrix(b)
    m1 += m2
    assert(m1.get_data() == [[5, 4], [6, 5], [0, 9]])
    assert(m2.get_data() == b)
def test___newsub__():
    m1 = MyMatrix(b)
    m2 = MyMatrix(a)
    m2 -= m1
    assert(m2.get_data() == [[-1, 0], [-4, -3], [0, -1]])
    assert (m1.get_data() == b)
def test_size():
    m1=MyMatrix(a)
    m2=MyMatrix(c)
    assert(m1.size() == (3,2))
    assert(m2.size() == (0,0))
def test_flip_left_right():
    m1=MyMatrix(a)
    m2=MyMatrix(c)
    res1=m1.flip_left_right()
    res2=m2.flip_left_right()
    assert(res1.get_data() == [[2,2],[1,1],[4,0]])
    assert(res2.get_data() == [])
def test_flip_up_down():
    m1=MyMatrix(a)
    m2=MyMatrix(c)
    res1=m1.flip_up_down()
    res2=m2.flip_up_down()
    assert(res1.get_data() == [[0,4],[1,1],[2,2]])
    assert(res2.get_data() == [])
def test_flipped_up_down():
    m1=MyMatrix(a)
    m2=MyMatrix(c)
    res1=m1.flipped_up_down()
    res2=m2.flipped_up_down()
    assert(res1.get_data() == [[0,4],[1,1],[2,2]])
    assert(res2.get_data() == [])
    assert(m1.get_data() == [[2, 2], [1, 1], [0, 4]])
def test_flipped_left_right():
    m1=MyMatrix(a)
    m2=MyMatrix(c)
    res1=m1.flipped_left_right()
    res2=m2.flipped_left_right()
    assert(res1.get_data() == [[2,2],[1,1],[4,0]])
    assert(res2.get_data() == [])
    assert(m1.get_data()==[[2, 2], [1, 1], [0, 4]])

def test_transpose():
    m1=MyMatrix(a)
    m2=MyMatrix(c)
    res1=m1.transpose()
    res2=m2.transpose()
    assert(res1.get_data() ==[[2,1,0],[2,1,4]])
    assert(res2.get_data() == [])

def test_transposed():
    m1=MyMatrix(a)
    m2=MyMatrix(c)
    res1=m1.transposed()
    res2=m2.transposed()
    assert(res1.get_data() ==[[2,1,0],[2,1,4]])
    assert(res2.get_data() == [])
    assert(m1.get_data() == [[2, 2], [1, 1], [0, 4]])



