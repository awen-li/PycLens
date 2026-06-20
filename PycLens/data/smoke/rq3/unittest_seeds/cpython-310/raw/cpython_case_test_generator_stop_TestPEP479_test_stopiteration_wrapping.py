# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_generator_stop.py
# case: TestPEP479_test_stopiteration_wrapping

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        raise StopIteration

    def g():
        yield f()
    with self.assertRaisesRegex(RuntimeError, 'generator raised StopIteration'):
        next(g())
