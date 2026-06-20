# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_richcmp.py
# case: MiscTest_test_recursion

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from collections import UserList
    a = UserList()
    b = UserList()
    a.append(b)
    b.append(a)
    self.assertRaises(RecursionError, operator.eq, a, b)
    self.assertRaises(RecursionError, operator.ne, a, b)
    self.assertRaises(RecursionError, operator.lt, a, b)
    self.assertRaises(RecursionError, operator.le, a, b)
    self.assertRaises(RecursionError, operator.gt, a, b)
    self.assertRaises(RecursionError, operator.ge, a, b)
    b.append(17)
    self.assertTrue(not a == b)
    self.assertTrue(a != b)
    self.assertRaises(RecursionError, operator.lt, a, b)
    self.assertRaises(RecursionError, operator.le, a, b)
    self.assertRaises(RecursionError, operator.gt, a, b)
    self.assertRaises(RecursionError, operator.ge, a, b)
    a.append(17)
    self.assertRaises(RecursionError, operator.eq, a, b)
    self.assertRaises(RecursionError, operator.ne, a, b)
    a.insert(0, 11)
    b.insert(0, 12)
    self.assertTrue(not a == b)
    self.assertTrue(a != b)
    self.assertTrue(a < b)
