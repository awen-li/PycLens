# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_swap_item

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    D = {'x': 1}
    with support.swap_item(D, 'x', 5) as x:
        self.assertEqual(D['x'], 5)
        self.assertEqual(x, 1)
    self.assertEqual(D['x'], 1)
    with support.swap_item(D, 'y', 5) as y:
        self.assertEqual(D['y'], 5)
        self.assertIsNone(y)
    self.assertNotIn('y', D)
    with support.swap_item(D, 'y', 5):
        del D['y']
    self.assertNotIn('y', D)
