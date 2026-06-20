# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_weakref

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = array.array(self.typecode, self.example)
    p = weakref.proxy(s)
    self.assertEqual(p.tobytes(), s.tobytes())
    s = None
    support.gc_collect()
    self.assertRaises(ReferenceError, len, p)
