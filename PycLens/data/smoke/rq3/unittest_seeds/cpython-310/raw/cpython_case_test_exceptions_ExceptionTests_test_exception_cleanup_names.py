# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_exception_cleanup_names

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        raise Exception()
    except Exception as e:
        self.assertIsInstance(e, Exception)
    self.assertNotIn('e', locals())
    with self.assertRaises(UnboundLocalError):
        e
