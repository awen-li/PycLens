# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_raise.py
# case: TestRaise_test_raise_from_None

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        try:
            raise TypeError('foo')
        except:
            raise ValueError() from None
    except ValueError as e:
        self.assertIsInstance(e.__context__, TypeError)
        self.assertIsNone(e.__cause__)
