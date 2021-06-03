class mymathlib():
    def __init__(self):
        '''Constructore for this class'''
        print('Creating object:', self.__class__.__name__)
    def add(self,x,y):
        return (x+y)
    def mul(self,x,y):
        return (x*y)
    def sub(self,x,y):
        return (x-y)
    def div(self,x,y):
        return (x/y)
    def __del__(self):
        '''Distrector of this class'''
        print('Deleting object:',self.__class__.__name__)
        
# x = mymathlib()
# print(x.add(3,4))