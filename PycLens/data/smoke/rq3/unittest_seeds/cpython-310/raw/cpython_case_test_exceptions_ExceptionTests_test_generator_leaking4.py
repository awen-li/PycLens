# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_generator_leaking4

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def g():
        try:
            1 / 0
        except ZeroDivisionError:
            yield sys.exc_info()[0]
            raise
    it = g()
    try:
        raise TypeError
    except TypeError:
        tp = next(it)
    self.assertIs(tp, ZeroDivisionError)
    try:
        next(it)
    except ZeroDivisionError as e:
        self.assertIs(sys.exc_info()[1], e)
    self.assertEqual(sys.exc_info(), (None, None, None))
