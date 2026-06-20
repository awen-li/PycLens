# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_raise.py
# case: TestRaise_test_yield_reraise

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def reraise():
        try:
            raise TypeError('foo')
        except:
            yield 1
            raise
    g = reraise()
    next(g)
    self.assertRaises(TypeError, lambda : next(g))
    self.assertRaises(StopIteration, lambda : next(g))
