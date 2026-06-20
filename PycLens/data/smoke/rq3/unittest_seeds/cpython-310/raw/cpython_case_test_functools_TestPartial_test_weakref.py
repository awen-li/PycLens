# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartial_test_weakref

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.partial(int, base=16)
    p = proxy(f)
    self.assertEqual(f.func, p.func)
    f = None
    support.gc_collect()
    self.assertRaises(ReferenceError, getattr, p, 'func')
