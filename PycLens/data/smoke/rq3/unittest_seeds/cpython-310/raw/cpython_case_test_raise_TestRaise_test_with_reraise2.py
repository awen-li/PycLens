# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_raise.py
# case: TestRaise_test_with_reraise2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def reraise():
        try:
            raise TypeError('foo')
        except:
            with Context():
                raise KeyError('caught')
            raise
    self.assertRaises(TypeError, reraise)
