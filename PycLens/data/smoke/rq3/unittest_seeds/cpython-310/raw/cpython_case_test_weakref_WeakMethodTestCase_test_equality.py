# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: WeakMethodTestCase_test_equality

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def _eq(a, b):
        self.assertTrue(a == b)
        self.assertFalse(a != b)

    def _ne(a, b):
        self.assertTrue(a != b)
        self.assertFalse(a == b)
    x = Object(1)
    y = Object(1)
    a = weakref.WeakMethod(x.some_method)
    b = weakref.WeakMethod(y.some_method)
    c = weakref.WeakMethod(x.other_method)
    d = weakref.WeakMethod(y.other_method)
    _eq(a, b)
    _eq(c, d)
    _ne(a, c)
    _ne(a, d)
    _ne(b, c)
    _ne(b, d)
    z = Object(2)
    e = weakref.WeakMethod(z.some_method)
    f = weakref.WeakMethod(z.other_method)
    _ne(a, e)
    _ne(a, f)
    _ne(b, e)
    _ne(b, f)
    _ne(a, x.some_method)
    _eq(a, ALWAYS_EQ)
    del x, y, z
    gc.collect()
    refs = (a, b, c, d, e, f)
    for q in refs:
        for r in refs:
            self.assertEqual(q == r, q is r)
            self.assertEqual(q != r, q is not r)
