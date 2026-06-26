# Source Generated with Decompyle++
# File: cpython-39-d6e24fa7ea2c.pyc (Python 3.9)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    
    class MainError(Exception):
        pass

    
    class SubError(Exception):
        pass

    
    def main():
        
        try:
            raise MainError()
        finally:
            pass
        if MainError:
            
            try:
                yield None
            finally:
                pass

            raise 
        return None


    coro = main()
    return None
    None(None)
    with self.assertRaises(MainError):
        coro.throw(SubError())
        None(None, None, None)
    with None:
        if not None:
            pass

if __name__ == '__main__':
    __pybcsec_seed__()
