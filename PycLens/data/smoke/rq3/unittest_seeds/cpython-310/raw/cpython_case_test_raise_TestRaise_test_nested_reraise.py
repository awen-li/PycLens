# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_raise.py
# case: TestRaise_test_nested_reraise

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def nested_reraise():
        raise

    def reraise():
        try:
            raise TypeError('foo')
        except:
            nested_reraise()
    self.assertRaises(TypeError, reraise)
