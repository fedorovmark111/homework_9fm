import copy
class MyMatrix:
    def __init__(self, data):
        """
        Create matrix of given data.
        Example of data:
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
        ]
        Return TypeError if data is not list.
        """
        self.__data = copy.deepcopy(data)
        

    def __repr__(self) -> str:
        m4=''
        for i in range(len(self.__data)):
            m4=m4+'\n'
            for j in range(len(self.__data[i])):
                m4=m4+str(self.__data[i][j])
                m4=m4+' '
        return m4

    def size(self) -> tuple:

        return len(self.__data), len(self.__data[0])
       

    def flip_up_down(self):

        for i in range(len(self.__data)//2):
            
            self.__data[i],self.__data[-i-1] = self.__data[-i-1],self.__data[i]
        return self
    
    
    def flip_left_right(self):

        for i in range(len(self.__data)):
            for j in range(len(self.__data[i])//2):
                self.__data[i][j],self.__data[i][-j-1] = self.__data[i][-j-1],self.__data[i][j]
        return self

    # методы flip_ ИЗМЕНЯЮТ матрицу
    # методы flipped_ по сути делают то же самое,
    # но возвращают изменённую КОПИЮ матрицы
    def flipped_up_down(self):

        sdd = copy.deepcopy(self.__data)
        sdd = MyMatrix(sdd)
        s = sdd.flip_up_down()
        return s
    def flipped_left_right(self):
        ss = copy.deepcopy(self.__data)
        ss = MyMatrix(ss)
        s1 = ss.flip_left_right()
        return s1

    def transpose(self):
        """
        E.g. modify
                          1, 5
        1, 2, 3, 4   to   2, 6
        5, 6, 7, 8        3, 7
                          4, 8
        """
        result = [[0 for i in range(len(self.__data))] for j in range(len(self.__data[0]))]
        for i in range(len(self.__data)):
            for j in range(len(self.__data[i])):
                result[j][i] = self.__data[i][j]
        self.__data=result
        return self
        
        
    def transposed(self):
        """
        Return transposed copy of MyMatrix.
        """
        sss = copy.deepcopy(self.__data)
        sss = MyMatrix(sss)
        ss1 = sss.transpose()
        return ss1
	
    def get_data(self) -> list:
        return self.__data
    def add(self, other):
        if len(self.__data) == len(other.__data) and len(self.__data[0]) == len(other.__data[0]):
            result = [[0 for i in range(len(self.__data[0]))] for j in range(len(self.__data))]
            for i in range(len(self.__data)):
                for j in range(len(self.__data[0])):
                    result[i][j] = self.__data[i][j] + other.__data[i][j]
            return MyMatrix(result)
        else:
            raise MatrixError('sizes are different')
    def sub(self, other):
        if len(self.__data) == len(other.__data) and len(self.__data[0]) == len(other.__data[0]):
            result = [[0 for i in range(len(self.__data[0]))] for j in range(len(self.__data))]
            for i in range(len(self.__data)):
                for j in range(len(self.__data[0])):
                    result[i][j] = self.__data[i][j] - other.__data[i][j]
            return MyMatrix(result)
        else:
            raise MatrixError('sizes are different')
    
    def new_add(self, other):
        """self += other."""
        return self+other
        
    def new_sub(self, other):  
        """self -= other."""
        return self-other

sl= [[3, 5, 11, 8],[8, 9, 0, 4],[3, 4, 6, 7],[4, 8, 19, 1],[1, 2, 3, 4]]
sl1=[[33, 5, 1, 1],[1, 3, 0, 3],[3, 5, 4, 9],[1, 2, 9, 8],[0, 9, 6, 7]]
m = MyMatrix(sl)
m4 = MyMatrix(sl1)
m1=(m.flipped_up_down())
print(m1.__repr__())
print(m.size())
m2=(m.flipped_left_right())
print(m2.__repr__())
m3=(m.transposed())
print(m3.__repr__())
m5=m.add(m4)
m6=m.sub(m4)
print(m5.__repr__())
print(m6.__repr__())
