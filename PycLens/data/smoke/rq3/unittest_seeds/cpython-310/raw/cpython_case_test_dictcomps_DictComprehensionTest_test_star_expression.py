# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dictcomps.py
# case: DictComprehensionTest_test_star_expression

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = {0: 0, 1: 1, 2: 4, 3: 9}
    self.assertEqual({i: i * i for i in [*range(4)]}, expected)
    self.assertEqual({i: i * i for i in (*range(4),)}, expected)
