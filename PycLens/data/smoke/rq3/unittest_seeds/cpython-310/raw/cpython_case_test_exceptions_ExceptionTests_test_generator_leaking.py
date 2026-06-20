# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_generator_leaking

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def yield_raise():
        try:
            raise KeyError('caught')
        except KeyError:
            yield sys.exc_info()[0]
            yield sys.exc_info()[0]
        yield sys.exc_info()[0]
    g = yield_raise()
    self.assertEqual(next(g), KeyError)
    self.assertEqual(sys.exc_info()[0], None)
    self.assertEqual(next(g), KeyError)
    self.assertEqual(sys.exc_info()[0], None)
    self.assertEqual(next(g), None)
    try:
        raise TypeError('foo')
    except TypeError:
        g = yield_raise()
        self.assertEqual(next(g), KeyError)
        self.assertEqual(sys.exc_info()[0], TypeError)
        self.assertEqual(next(g), KeyError)
        self.assertEqual(sys.exc_info()[0], TypeError)
        self.assertEqual(next(g), TypeError)
        del g
        self.assertEqual(sys.exc_info()[0], TypeError)
