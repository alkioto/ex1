print("Hello world !")

def xxx():
    def f1():
        ''' Привет! ЁЁЁ """" '''
        pass
    def f2():
        ''' ####
        """
        '''
        print("WWW")
        pass
    return f1,f2
        
a,b = xxx()
a.__doc__
b()
b.__doc__
