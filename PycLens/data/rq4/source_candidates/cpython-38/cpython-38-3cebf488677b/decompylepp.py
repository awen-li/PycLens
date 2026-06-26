# Source Generated with Decompyle++
# File: cpython-38-3cebf488677b.pyc (Python 3.8)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    
    class TestException(MemoryError):
        pass

    
    try:
        raise MemoryError
    finally:
        pass
    exc = None << (None ^= (NoneDELETE_SUBSCRMemoryError))
    
    try:
        inst = exc
    finally:
        if None:
            exc = None
            del exc
        
        
        try:
            raise TestException
        finally:
            pass
        except Exception:
            pass
        

        for _ in range(10):
            
            try:
                raise MemoryError
            finally:
                pass
            except MemoryError:
                exc = None
                
                try:
                    pass
                finally:
                    if None:
                        exc = None
                        del exc
                    
                    gc_collect()
                    continue
                    return None





if __name__ == '__main__':
    __pybcsec_seed__()
