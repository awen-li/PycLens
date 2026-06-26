# Source Generated with Decompyle++
# File: cpython-310-8f983d858481.pyc (Python 3.10)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = runtime_checkable(<NODE:12>)
    
    class C:
        pass

    
    class D:
        
        def meth(self):
            pass


    
    def f():
        pass

    self.assertIsSubclass(D, P)
    self.assertIsInstance(D(), P)
    self.assertNotIsSubclass(C, P)
    self.assertNotIsInstance(C(), P)
    self.assertNotIsSubclass(types.FunctionType, P)
    self.assertNotIsInstance(f, P)

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
