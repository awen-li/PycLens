# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_generator_stop.py
# case: TestPEP479_test_stopiteration_wrapping_context

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        raise StopIteration

    def g():
        yield f()
    try:
        next(g())
    except RuntimeError as exc:
        self.assertIs(type(exc.__cause__), StopIteration)
        self.assertIs(type(exc.__context__), StopIteration)
        self.assertTrue(exc.__suppress_context__)
    else:
        self.fail('__cause__, __context__, or __suppress_context__ were not properly set')
