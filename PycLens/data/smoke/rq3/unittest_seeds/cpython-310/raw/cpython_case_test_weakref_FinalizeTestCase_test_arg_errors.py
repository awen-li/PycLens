# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: FinalizeTestCase_test_arg_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def fin(*args, **kwargs):
        res.append((args, kwargs))
    a = self.A()
    res = []
    f = weakref.finalize(a, fin, 1, 2, func=3, obj=4)
    self.assertEqual(f.peek(), (a, fin, (1, 2), {'func': 3, 'obj': 4}))
    f()
    self.assertEqual(res, [((1, 2), {'func': 3, 'obj': 4})])
    with self.assertRaises(TypeError):
        weakref.finalize(a, func=fin, arg=1)
    with self.assertRaises(TypeError):
        weakref.finalize(obj=a, func=fin, arg=1)
    self.assertRaises(TypeError, weakref.finalize, a)
    self.assertRaises(TypeError, weakref.finalize)
