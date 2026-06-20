# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_marshal.py
# case: CodeTestCase_test_many_codeobjects

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    count = 5000
    codes = (ExceptionTestCase.test_exceptions.__code__,) * count
    marshal.loads(marshal.dumps(codes))
