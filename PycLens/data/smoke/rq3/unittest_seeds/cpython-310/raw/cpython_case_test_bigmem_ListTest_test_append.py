# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: ListTest_test_append

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    l = [object()] * size
    l.append(object())
    self.assertEqual(len(l), size + 1)
    self.assertTrue(l[-3] is l[-2])
    self.assertFalse(l[-2] is l[-1])
