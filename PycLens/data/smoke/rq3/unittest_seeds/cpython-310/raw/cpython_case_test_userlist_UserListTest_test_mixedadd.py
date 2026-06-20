# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_userlist.py
# case: UserListTest_test_mixedadd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    u = self.type2test([0, 1])
    self.assertEqual(u + [], u)
    self.assertEqual(u + [2], [0, 1, 2])
