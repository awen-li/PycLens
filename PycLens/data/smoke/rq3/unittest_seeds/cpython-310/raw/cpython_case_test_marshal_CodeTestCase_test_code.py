# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_marshal.py
# case: CodeTestCase_test_code

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    co = ExceptionTestCase.test_exceptions.__code__
    new = marshal.loads(marshal.dumps(co))
    self.assertEqual(co, new)
