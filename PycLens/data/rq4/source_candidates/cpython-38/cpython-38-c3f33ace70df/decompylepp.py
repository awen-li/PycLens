# Source Generated with Decompyle++
# File: cpython-38-c3f33ace70df.pyc (Python 3.8)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    trace = []
    
    def f(r):
        gi = g(r)
        next(gi)
        
        try:
            trace.append('f resuming g')
            next(gi)
            trace.append('f SHOULD NOT BE HERE')
        finally:
            pass
        except StopIteration:
            e = None
            
            try:
                trace.append('f caught %r' % (e,))
            finally:
                if None:
                    e = None
                    del e
                
                return None



    
    def g(r):
        trace.append('g starting')
        yield None
        trace.append('g returning %r' % (r,))
        return None()

    f(None)
    f(1)
    f((2,))
    f(StopIteration(3))
    self.assertEqual(trace, [
        'g starting',
        'f resuming g',
        'g returning None',
        'f caught StopIteration()',
        'g starting',
        'f resuming g',
        'g returning 1',
        'f caught StopIteration(1)',
        'g starting',
        'f resuming g',
        'g returning (2,)',
        'f caught StopIteration((2,))',
        'g starting',
        'f resuming g',
        'g returning StopIteration(3)',
        'f caught StopIteration(StopIteration(3))'])

if __name__ == '__main__':
    __pybcsec_seed__()
