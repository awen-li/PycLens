# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_slice.py
# case: SliceTest_test_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = slice(1, 10)
    c = copy.copy(s)
    self.assertIs(s, c)
    s = slice(1, 10, 2)
    c = copy.copy(s)
    self.assertIs(s, c)
    s = slice([1, 2], [3, 4], [5, 6])
    c = copy.copy(s)
    self.assertIs(s, c)
    self.assertIs(s.start, c.start)
    self.assertIs(s.stop, c.stop)
    self.assertIs(s.step, c.step)
