# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_userlist.py
# case: UserListTest_test_slice_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    l = [0, 1, 2, 3, 4]
    u = UserList(l)
    self.assertIsInstance(u[:], u.__class__)
    self.assertEqual(u[:], u)
