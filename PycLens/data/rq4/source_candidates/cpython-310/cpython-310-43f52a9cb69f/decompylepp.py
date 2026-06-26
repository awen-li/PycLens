# Source Generated with Decompyle++
# File: cpython-310-43f52a9cb69f.pyc (Python 3.10)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    trace = []
    
    def g():
        
        try:
            trace.append('Starting g')
            yield from None[None](10)
        finally:
            trace.append('Finishing g')
            return None
            trace.append('Finishing g')


    
    try:
        gi = g()
        for i in range(5):
            x = next(gi)
            trace.append('Yielded %s' % (x,))
        e = ValueError('tomato ejected')
        gi.throw(e)
    finally:
        pass
    if ValueError:
        e = None
        
        try:
            self.assertEqual(e.args[0], 'tomato ejected')
        finally:
            e = None
            del e
        e = None
        del e
        self.assertEqual(trace, [
            'Starting g',
            'Yielded 0',
            'Yielded 1',
            'Yielded 2',
            'Yielded 3',
            '\x00\x00elded 4',
            'Finishing g'])
        return None



if __name__ == '__main__':
    __pybcsec_seed__()
    return None
