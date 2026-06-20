# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestSubclass_test_weakref

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = deque('gallahad')
    p = weakref.proxy(d)
    self.assertEqual(str(p), str(d))
    d = None
    support.gc_collect()
    self.assertRaises(ReferenceError, str, p)
