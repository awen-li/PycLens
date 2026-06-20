# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_call.py
# case: FastCallTests_test_vectorcall_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (func, args, expected) in self.CALLS_POSARGS:
        with self.subTest(func=func, args=args):
            result = _testcapi.pyobject_fastcalldict(func, args, None)
            self.check_result(result, expected)
            if not args:
                result = _testcapi.pyobject_fastcalldict(func, None, None)
                self.check_result(result, expected)
    for (func, args, kwargs, expected) in self.CALLS_KWARGS:
        with self.subTest(func=func, args=args, kwargs=kwargs):
            result = _testcapi.pyobject_fastcalldict(func, args, kwargs)
            self.check_result(result, expected)
