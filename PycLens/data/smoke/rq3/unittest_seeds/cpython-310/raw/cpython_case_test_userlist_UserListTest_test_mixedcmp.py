# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_userlist.py
# case: UserListTest_test_mixedcmp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    u = self.type2test([0, 1])
    self.assertEqual(u, [0, 1])
    self.assertNotEqual(u, [0])
    self.assertNotEqual(u, [0, 2])
