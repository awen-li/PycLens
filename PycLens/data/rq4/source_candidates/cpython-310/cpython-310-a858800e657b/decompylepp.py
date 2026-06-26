# Source Generated with Decompyle++
# File: cpython-310-a858800e657b.pyc (Python 3.10)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    trace = []
    
    def g1():
        global append
        
        try:
            trace.append('Starting g1')
            if None:
                del append
                yield from g2()
                yield 'g1 eggs'
        finally:
            trace.append('Finishing g1')
            return None
            trace.append('Finishing g1')


    
    def g2():
        
        try:
            trace.append('Starting g2')
            yield 'g2 spam'
            None = None
            raise None(None)
            trace.append('Finishing g2')


    
    try:
        for x in g1():
            (None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, trace.append, 'Yielded %s', x)
    finally:
        pass
    if ValueError:
        e = None
        
        try:
            self.assertEqual(e.args[0], 'hovercraft is full of eels')
        finally:
            e = None
            del e
        e = None
        del e
        self.assertEqual(trace, [
            'Starting g1',
            'Yielded g1 ham',
            'Starting g2',
            'Yielded g2 spam',
            'Finishing g2',
            'Finishing g1'])
        return None



if __name__ == '__main__':
    __pybcsec_seed__()
    return None
