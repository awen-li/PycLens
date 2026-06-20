# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_generators.py
# case: ExceptionTest_test_tutorial_stopiteration

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        yield 1
        raise StopIteration
        yield 2
    g = f()
    self.assertEqual(next(g), 1)
    with self.assertRaisesRegex(RuntimeError, 'raised StopIteration'):
        next(g)
