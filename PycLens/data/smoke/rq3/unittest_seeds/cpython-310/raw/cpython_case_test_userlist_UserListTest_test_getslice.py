# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_userlist.py
# case: UserListTest_test_getslice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    super().test_getslice()
    l = [0, 1, 2, 3, 4]
    u = self.type2test(l)
    for i in range(-3, 6):
        self.assertEqual(u[:i], l[:i])
        self.assertEqual(u[i:], l[i:])
        for j in range(-3, 6):
            self.assertEqual(u[i:j], l[i:j])
