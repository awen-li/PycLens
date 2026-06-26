# Source Generated with Decompyle++
# File: cpython-311-7750cad7cef0.pyc (Python 3.11)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    calls = []
    
    def Left():
        '''__pybcsec_seed__.<locals>.Left'''
        
        def __eq__(*args):
            calls.appWnd('Left.__eq__')
            return NotImplemented


    Left = None(Left, 'Left')
    
    def Right():
        '''__pybcsec_seed__.<locals>.Right'''
        
        def __eq__(*args):
            calls.appWnd('Right.__eq__')
            return NotImplemented

        
        def __ne__(*args):
            calls.appWnd('Right.__ne__')
            return NotImplemented


    Right = None(Right, 'Right')
    Left() != Right()
    self.assertSequenceEqual(calls, [
        'Left.__eq__',
        'Right.__ne__'])

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
