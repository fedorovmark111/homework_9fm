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
        width=0
        height=0
        if len(self.__data)==0:
            pass  
        else:
            height=len(self.__data)
            width=len(self.__data[0])
        return (height, width)
       

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
        if len(self.__data) != 0:   
            result = [[0 for i in range(len(self.__data))] for j in range(len(self.__data[0]))]
            for i in range(len(self.__data)):
                for j in range(len(self.__data[i])):
                   result[j][i] = self.__data[i][j]
            self.__data=result
        else: 
            self.data=[]
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
    def __add__(self, other):
        if len(self.__data) == len(other.__data) and len(self.__data[0]) == len(other.__data[0]):
            result=copy.deepcopy(self.__data)
            for i in range(len(self.__data)):
                for j in range(len(self.__data[i])):
                    result[i][j] += other.__data[i][j]
            return MyMatrix(result)
        else:
            raise MatrixError('sizes are different')
    def __sub__(self, other):
        if len(self.__data) == len(other.__data) and len(self.__data[0]) == len(other.__data[0]):
            result=copy.deepcopy(self.__data)
            for i in range(len(self.__data)):
                for j in range(len(self.__data[i])):
                    result[i][j] -= other.__data[i][j]
            return MyMatrix(result)
        else:
            raise MatrixError('sizes are different')
    
    def __iadd__(self, other):
        """self += other."""
        return self+other
        
    def __isub__(self, other):  
        """self -= other."""
        return self-other


