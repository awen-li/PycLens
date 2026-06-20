# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_raise.py
# case: TestRaise_test_reraise

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        try:
            raise IndexError()
        except IndexError as e:
            exc1 = e
            raise
    except IndexError as exc2:
        self.assertIs(exc1, exc2)
    else:
        self.fail('No exception raised')
