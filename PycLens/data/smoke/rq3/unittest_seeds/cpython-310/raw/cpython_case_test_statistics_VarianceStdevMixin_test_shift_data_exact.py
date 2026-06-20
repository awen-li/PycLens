# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: VarianceStdevMixin_test_shift_data_exact

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raw = [1, 3, 3, 4, 5, 7, 9, 10, 11, 16]
    assert all((x == int(x) for x in raw))
    expected = self.func(raw)
    shift = 10 ** 9
    data = [x + shift for x in raw]
    self.assertEqual(self.func(data), expected)
