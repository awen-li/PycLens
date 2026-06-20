# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_marshal.py
# case: ExceptionTestCase_test_exceptions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    new = marshal.loads(marshal.dumps(StopIteration))
    self.assertEqual(StopIteration, new)
