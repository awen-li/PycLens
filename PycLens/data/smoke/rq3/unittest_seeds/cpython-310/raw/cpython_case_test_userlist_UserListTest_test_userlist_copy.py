# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_userlist.py
# case: UserListTest_test_userlist_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    u = self.type2test([6, 8, 1, 9, 1])
    v = u.copy()
    self.assertEqual(u, v)
    self.assertEqual(type(u), type(v))
