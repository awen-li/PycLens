# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_add

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = deque()
    e = deque('abc')
    f = deque('def')
    self.assertEqual(d + d, deque())
    self.assertEqual(e + f, deque('abcdef'))
    self.assertEqual(e + e, deque('abcabc'))
    self.assertEqual(e + d, deque('abc'))
    self.assertEqual(d + e, deque('abc'))
    self.assertIsNot(d + d, deque())
    self.assertIsNot(e + d, deque('abc'))
    self.assertIsNot(d + e, deque('abc'))
    g = deque('abcdef', maxlen=4)
    h = deque('gh')
    self.assertEqual(g + h, deque('efgh'))
    with self.assertRaises(TypeError):
        deque('abc') + 'def'
