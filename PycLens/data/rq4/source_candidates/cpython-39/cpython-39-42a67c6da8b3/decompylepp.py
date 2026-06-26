# Source Generated with Decompyle++
# File: cpython-39-42a67c6da8b3.pyc (Python 3.9)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    
    def store_raise_exc_generator():
        
        try:
            None(self.assertEqual(sys.exc_info)[0], None)
            yield None
        finally:
            pass
        if Exception:
            exc = None
            
            try:
                self.assertEqual(sys.exc_info()[0], ValueError)
                self.assertIsNone(exc.__context__)
                yield None
                self.assertEqual(sys.exc_info()[0], ValueError)
                yield None
                raise 
            finally:
                exc = None
                del exc
            exc = None
            del exc
            return None



    make = store_raise_exc_generator()
    if not None:
        None(make)
        
        try:
            raise ValueError()
        finally:
            pass
        if Exception:
            exc = None
            
            try:
                
                try:
                    make.throw(exc)
                finally:
                    pass
                if Exception:
                    pass
                finally:
                    exc = None
                    del exc
                exc = None
                del exc
                with self.assertRaises(ValueError) as cm:
                    next(make)
                    Exception(None, None, None)
                with None:
                    if not None:
                        pass

                self.assertIsNone(cm.exception.__context__)
                self.assertEqual(sys.exc_info(), (None, None, None))
                return None



if __name__ == '__main__':
    __pybcsec_seed__()
