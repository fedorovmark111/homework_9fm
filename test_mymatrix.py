from mymatrix import MyMatrix
a=[[1, 2], [3, 4], [4, 5]]
b=[[7, 2], [5, 4], [0, 5]]
def test___add__():
    matrix1 = MyMatrix(a)
    matrix2 = MyMatrix(b)
    summatrix = matrix1 + matrix2
    assert(summatrix.get_data() == [[8, 4], [8, 8], [4, 10]])
    assert(matrix1.get_data()== a)
    assert (matrix2.get_data() == b)

def test___sub__():
    matrix2 = MyMatrix(a)
    matrix1 = MyMatrix(b)
    submatrix = matrix1 - matrix2
    assert(submatrix.get_data() == [[6, 0], [2, 0], [-4, 0]])
    assert (matrix1.get_data() == b)
    assert (matrix2.get_data() == a)

def test___newadd__():
    matrix1 = MyMatrix(a)
    matrix2 = MyMatrix(b)
    matrix1 += matrix2
    assert(matrix1.get_data() == [[8, 4], [8, 8], [4, 10]])
    assert(matrix2.get_data() == b)
def test___newsub__():
    matrix1 = MyMatrix(b)
    matrix2 = MyMatrix(a)
    matrix1 -= matrix2
    assert(matrix1.get_data() == [[6, 0], [2, 0], [-4, 0]])
    assert (matrix2.get_data() == a)



