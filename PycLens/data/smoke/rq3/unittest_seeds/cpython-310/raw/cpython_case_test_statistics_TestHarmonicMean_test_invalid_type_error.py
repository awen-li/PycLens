# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestHarmonicMean_test_invalid_type_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for data in [['3.14'], ['1', '2', '3'], [1, '2', 3, '4', 5], [2.3, 3.4, 4.5, '5.6']]:
        with self.subTest(data=data):
            with self.assertRaises(TypeError):
                self.func(data)
