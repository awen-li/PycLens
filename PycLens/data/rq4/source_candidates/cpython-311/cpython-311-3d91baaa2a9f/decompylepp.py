# Source Generated with Decompyle++
# File: cpython-311-3d91baaa2a9f.pyc (Python 3.11)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    calls = []
    
    def Base():
        '''__pybcsec_seed__.<locals>.Base'''
        pass

    Base = None(Base, 'Base')
    
    def Derived():
        '''__pybcsec_seed__.<locals>.Derived'''
        
        def __eq__(*args):
            calls.append('Derived.__eq__')
            return NotImplemented

        
        def __ne__(*args):
            calls.append('Derived.__ne__')
            return NotImplemented


    Derived = None(Derived, 'Derived', Base)
    Base() != Derived()
    self.assertSequenceEqual(calls, [
        'Derived.__ne__',
        'Base.__eq__'])

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
