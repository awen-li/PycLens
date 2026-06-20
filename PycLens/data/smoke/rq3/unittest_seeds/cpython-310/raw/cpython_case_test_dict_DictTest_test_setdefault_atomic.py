# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_setdefault_atomic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Hashed(object):

        def __init__(self):
            self.hash_count = 0
            self.eq_count = 0

        def __hash__(self):
            self.hash_count += 1
            return 42

        def __eq__(self, other):
            self.eq_count += 1
            return id(self) == id(other)
    hashed1 = Hashed()
    y = {hashed1: 5}
    hashed2 = Hashed()
    y.setdefault(hashed2, [])
    self.assertEqual(hashed1.hash_count, 1)
    self.assertEqual(hashed2.hash_count, 1)
    self.assertEqual(hashed1.eq_count + hashed2.eq_count, 1)
