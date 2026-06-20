# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_raise.py
# case: TestContext_test_c_exception_raise

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        try:
            1 / 0
        except:
            xyzzy
    except NameError as e:
        self.assertIsInstance(e.__context__, ZeroDivisionError)
    else:
        self.fail('No exception raised')
