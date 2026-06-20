# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_comparisons

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = deque('xabc')
    d.popleft()
    for e in [d, deque('abc'), deque('ab'), deque(), list(d)]:
        self.assertEqual(d == e, type(d) == type(e) and list(d) == list(e))
        self.assertEqual(d != e, not (type(d) == type(e) and list(d) == list(e)))
    args = map(deque, ('', 'a', 'b', 'ab', 'ba', 'abc', 'xba', 'xabc', 'cba'))
    for x in args:
        for y in args:
            self.assertEqual(x == y, list(x) == list(y), (x, y))
            self.assertEqual(x != y, list(x) != list(y), (x, y))
            self.assertEqual(x < y, list(x) < list(y), (x, y))
            self.assertEqual(x <= y, list(x) <= list(y), (x, y))
            self.assertEqual(x > y, list(x) > list(y), (x, y))
            self.assertEqual(x >= y, list(x) >= list(y), (x, y))
