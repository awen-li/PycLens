# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_dictview_set_operations_on_items

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    k1 = {1: 1, 2: 2}.items()
    k2 = {1: 1, 2: 2, 3: 3}.items()
    k3 = {4: 4}.items()
    self.assertEqual(k1 - k2, set())
    self.assertEqual(k1 - k3, {(1, 1), (2, 2)})
    self.assertEqual(k2 - k1, {(3, 3)})
    self.assertEqual(k3 - k1, {(4, 4)})
    self.assertEqual(k1 & k2, {(1, 1), (2, 2)})
    self.assertEqual(k1 & k3, set())
    self.assertEqual(k1 | k2, {(1, 1), (2, 2), (3, 3)})
    self.assertEqual(k1 ^ k2, {(3, 3)})
    self.assertEqual(k1 ^ k3, {(1, 1), (2, 2), (4, 4)})
