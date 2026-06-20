# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestSet_test_weakref

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = self.thetype('gallahad')
    p = weakref.proxy(s)
    self.assertEqual(str(p), str(s))
    s = None
    support.gc_collect()
    self.assertRaises(ReferenceError, str, p)
