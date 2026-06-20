# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestMedian_test_even_ints

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [1, 2, 3, 4, 5, 6]
    assert len(data) % 2 == 0
    self.assertEqual(self.func(data), 3.5)
