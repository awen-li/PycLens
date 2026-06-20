# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_generators.py
# case: ExceptionTest_test_except_throw_exception_context

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def gen():
        try:
            try:
                self.assertEqual(sys.exc_info()[0], None)
                yield
            except ValueError:
                self.assertEqual(sys.exc_info()[0], ValueError)
                raise TypeError()
        except Exception as exc:
            self.assertEqual(sys.exc_info()[0], TypeError)
            self.assertEqual(type(exc.__context__), ValueError)
        self.assertEqual(sys.exc_info()[0], ValueError)
        yield
        self.assertIsNone(sys.exc_info()[0])
        yield 'done'
    g = gen()
    next(g)
    try:
        raise ValueError
    except Exception as exc:
        g.throw(exc)
    self.assertEqual(next(g), 'done')
    self.assertEqual(sys.exc_info(), (None, None, None))
