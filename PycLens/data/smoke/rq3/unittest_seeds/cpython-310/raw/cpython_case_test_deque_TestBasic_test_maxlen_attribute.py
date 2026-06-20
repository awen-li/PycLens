# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_maxlen_attribute

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(deque().maxlen, None)
    self.assertEqual(deque('abc').maxlen, None)
    self.assertEqual(deque('abc', maxlen=4).maxlen, 4)
    self.assertEqual(deque('abc', maxlen=2).maxlen, 2)
    self.assertEqual(deque('abc', maxlen=0).maxlen, 0)
    with self.assertRaises(AttributeError):
        d = deque('abc')
        d.maxlen = 10
