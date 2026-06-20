# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_userlist.py
# case: UserListTest_test_radd_specials

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    u = UserList('eggs')
    u2 = 'spam' + u
    self.assertEqual(u2, list('spameggs'))
    u2 = u.__radd__(UserList('spam'))
    self.assertEqual(u2, list('spameggs'))
