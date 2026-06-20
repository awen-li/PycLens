# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_userlist.py
# case: UserListTest_test_getitemoverwriteiter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class T(self.type2test):

        def __getitem__(self, key):
            return str(key) + '!!!'
    self.assertEqual(next(iter(T((1, 2)))), '0!!!')
