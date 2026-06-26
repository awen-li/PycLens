# Source Generated with Decompyle++
# File: cpython-312-c82319e42246.pyc (Python 3.12)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    
    class filelike:
        
        def __init__(self):
            self.written = ''
            self.flushed = 0

        
        def write(self, str):
            pass

        
        def flush(self):
            pass


    f = filelike()
    print(1, file = f, end = '', flush = True)
    print(2, file = f, end = '', flush = True)
    print(3, file = f, flush = False)
    self.assertEqual(f.written, '123\n')
    self.assertEqual(f.flushed, 2)
    
    class noflush:
        
        def write(self, str):
            pass

        
        def flush(self):
            raise RuntimeError


    self.assertRaises(RuntimeError, print, 1, file = noflush(), flush = True)

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
