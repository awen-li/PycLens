# Source Generated with Decompyle++
# File: cpython-38-c8d67b905643.pyc (Python 3.8)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    
    def f():
        raise StopIteration

    
    def g():
        yield f()

    
    try:
        next(g())
    finally:
        pass
    except RuntimeError:
        (None,)
        exc = (None,)
        
        try:
            self.assertIs(type(exc.__cause__), StopIteration)
            self.assertIs(type(exc.__context__), StopIteration)
            self.assertTrue(exc.__suppress_context__)
        finally:
            if None:
                exc = None
                del exc
            
            return None



if __name__ == '__main__':
    __pybcsec_seed__()
