# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_generator_doesnt_retain_old_exc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def g():
        self.assertIsInstance(sys.exc_info()[1], RuntimeError)
        yield
        self.assertEqual(sys.exc_info(), (None, None, None))
    it = g()
    try:
        raise RuntimeError
    except RuntimeError:
        next(it)
    self.assertRaises(StopIteration, next, it)
