# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dictviews.py
# case: DictSetTest_test_compare_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Exc(Exception):
        pass

    class BadEq:

        def __hash__(self):
            return 7

        def __eq__(self, other):
            raise Exc
    (k1, k2) = (BadEq(), BadEq())
    (v1, v2) = (BadEq(), BadEq())
    d = {k1: v1}
    self.assertIn(k1, d)
    self.assertIn(k1, d.keys())
    self.assertIn(v1, d.values())
    self.assertIn((k1, v1), d.items())
    self.assertRaises(Exc, d.__contains__, k2)
    self.assertRaises(Exc, d.keys().__contains__, k2)
    self.assertRaises(Exc, d.items().__contains__, (k2, v1))
    self.assertRaises(Exc, d.items().__contains__, (k1, v2))
    with self.assertRaises(Exc):
        v2 in d.values()
