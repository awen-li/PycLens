# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartial_test_positional

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for args in [(), (0,), (0, 1), (0, 1, 2), (0, 1, 2, 3)]:
        p = self.partial(capture, *args)
        expected = args + ('x',)
        (got, empty) = p('x')
        self.assertTrue(expected == got and empty == {})
