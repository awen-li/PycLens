# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: VarianceStdevMixin_test_shift_data

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raw = [1.03, 1.27, 1.94, 2.04, 2.58, 3.14, 4.75, 4.98, 5.42, 6.78]
    expected = self.func(raw)
    shift = 100000.0
    data = [x + shift for x in raw]
    self.assertApproxEqual(self.func(data), expected)
