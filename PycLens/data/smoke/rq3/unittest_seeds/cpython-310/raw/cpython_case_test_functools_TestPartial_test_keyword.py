# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartial_test_keyword

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for a in ['a', 0, None, 3.5]:
        p = self.partial(capture, a=a)
        expected = {'a': a, 'x': None}
        (empty, got) = p(x=None)
        self.assertTrue(expected == got and empty == ())
