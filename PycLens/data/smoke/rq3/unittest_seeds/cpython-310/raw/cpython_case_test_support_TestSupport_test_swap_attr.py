# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_swap_attr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Obj:
        pass
    obj = Obj()
    obj.x = 1
    with support.swap_attr(obj, 'x', 5) as x:
        self.assertEqual(obj.x, 5)
        self.assertEqual(x, 1)
    self.assertEqual(obj.x, 1)
    with support.swap_attr(obj, 'y', 5) as y:
        self.assertEqual(obj.y, 5)
        self.assertIsNone(y)
    self.assertFalse(hasattr(obj, 'y'))
    with support.swap_attr(obj, 'y', 5):
        del obj.y
    self.assertFalse(hasattr(obj, 'y'))
