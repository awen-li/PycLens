# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_assert_shadowing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    global AssertionError
    AssertionError = TypeError
    try:
        assert False, 'hello'
    except BaseException as e:
        del AssertionError
        self.assertIsInstance(e, AssertionError)
        self.assertEqual(str(e), 'hello')
    else:
        del AssertionError
        self.fail('Expected exception')
