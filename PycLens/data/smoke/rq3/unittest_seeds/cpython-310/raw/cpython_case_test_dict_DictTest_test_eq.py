# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_eq

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual({}, {})
    self.assertEqual({1: 2}, {1: 2})

    class Exc(Exception):
        pass

    class BadCmp(object):

        def __eq__(self, other):
            raise Exc()

        def __hash__(self):
            return 1
    d1 = {BadCmp(): 1}
    d2 = {1: 1}
    with self.assertRaises(Exc):
        d1 == d2
