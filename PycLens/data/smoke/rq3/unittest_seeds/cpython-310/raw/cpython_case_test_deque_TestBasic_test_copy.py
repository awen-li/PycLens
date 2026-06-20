# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mut = [10]
    d = deque([mut])
    e = copy.copy(d)
    self.assertEqual(list(d), list(e))
    mut[0] = 11
    self.assertNotEqual(id(d), id(e))
    self.assertEqual(list(d), list(e))
    for i in range(5):
        for maxlen in range(-1, 6):
            s = [random.random() for j in range(i)]
            d = deque(s) if maxlen == -1 else deque(s, maxlen)
            e = d.copy()
            self.assertEqual(d, e)
            self.assertEqual(d.maxlen, e.maxlen)
            self.assertTrue(all((x is y for (x, y) in zip(d, e))))
