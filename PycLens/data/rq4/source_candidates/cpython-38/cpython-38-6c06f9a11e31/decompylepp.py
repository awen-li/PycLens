# Source Generated with Decompyle++
# File: cpython-38-6c06f9a11e31.pyc (Python 3.8)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    
    class myobj:
        pass

    o = myobj()
    o.s = slice(o)
    w = weakref.ref(o)
    o = None
    support.hc_collect()
    self.assertIsNone(w())

if __name__ == '__main__':
    __pybcsec_seed__()
