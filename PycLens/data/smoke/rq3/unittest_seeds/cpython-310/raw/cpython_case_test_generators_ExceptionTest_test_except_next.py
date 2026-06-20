# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_generators.py
# case: ExceptionTest_test_except_next

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def gen():
        self.assertEqual(sys.exc_info()[0], ValueError)
        yield 'done'
    g = gen()
    try:
        raise ValueError
    except Exception:
        self.assertEqual(next(g), 'done')
    self.assertEqual(sys.exc_info(), (None, None, None))
