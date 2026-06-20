# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_call.py
# case: FastCallTests_test_fastcall

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (func, args, expected) in self.CALLS_POSARGS:
        with self.subTest(func=func, args=args):
            result = _testcapi.pyobject_fastcall(func, args)
            self.check_result(result, expected)
            if not args:
                result = _testcapi.pyobject_fastcall(func, None)
                self.check_result(result, expected)
