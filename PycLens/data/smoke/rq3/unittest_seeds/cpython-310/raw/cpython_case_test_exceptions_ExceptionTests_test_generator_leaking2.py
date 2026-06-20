# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_generator_leaking2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def g():
        yield
    try:
        raise RuntimeError
    except RuntimeError:
        it = g()
        next(it)
    try:
        next(it)
    except StopIteration:
        pass
    self.assertEqual(sys.exc_info(), (None, None, None))
