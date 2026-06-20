# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_raise_in_generator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def g():
        yield 1
        raise
        yield 2
    with self.assertRaises(ZeroDivisionError):
        i = g()
        try:
            1 / 0
        except:
            next(i)
            next(i)
