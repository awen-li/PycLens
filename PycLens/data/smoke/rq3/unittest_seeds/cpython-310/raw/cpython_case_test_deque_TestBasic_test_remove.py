# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_remove

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = deque('abcdefghcij')
    d.remove('c')
    self.assertEqual(d, deque('abdefghcij'))
    d.remove('c')
    self.assertEqual(d, deque('abdefghij'))
    self.assertRaises(ValueError, d.remove, 'c')
    self.assertEqual(d, deque('abdefghij'))
    d = deque(['a', 'b', BadCmp(), 'c'])
    e = deque(d)
    self.assertRaises(RuntimeError, d.remove, 'c')
    for (x, y) in zip(d, e):
        self.assertTrue(x is y)
    for match in (True, False):
        d = deque(['ab'])
        d.extend([MutateCmp(d, match), 'c'])
        self.assertRaises(IndexError, d.remove, 'c')
        self.assertEqual(d, deque())
