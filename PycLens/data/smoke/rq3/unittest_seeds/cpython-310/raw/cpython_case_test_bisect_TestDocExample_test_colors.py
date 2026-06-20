# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bisect.py
# case: TestDocExample_test_colors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [('red', 5), ('blue', 1), ('yellow', 8), ('black', 0)]
    data.sort(key=lambda r: r[1])
    keys = [r[1] for r in data]
    bisect_left = self.module.bisect_left
    self.assertEqual(data[bisect_left(keys, 0)], ('black', 0))
    self.assertEqual(data[bisect_left(keys, 1)], ('blue', 1))
    self.assertEqual(data[bisect_left(keys, 5)], ('red', 5))
    self.assertEqual(data[bisect_left(keys, 8)], ('yellow', 8))
