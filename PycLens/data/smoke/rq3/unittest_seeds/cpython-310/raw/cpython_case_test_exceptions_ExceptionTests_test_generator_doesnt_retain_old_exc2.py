# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_generator_doesnt_retain_old_exc2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def g():
        try:
            raise ValueError
        except ValueError:
            yield 1
        self.assertEqual(sys.exc_info(), (None, None, None))
        yield 2
    gen = g()
    try:
        raise IndexError
    except IndexError:
        self.assertEqual(next(gen), 1)
    self.assertEqual(next(gen), 2)
