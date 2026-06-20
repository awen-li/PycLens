# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_marshal.py
# case: CodeTestCase_test_different_filenames

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    co1 = compile('x', 'f1', 'exec')
    co2 = compile('y', 'f2', 'exec')
    (co1, co2) = marshal.loads(marshal.dumps((co1, co2)))
    self.assertEqual(co1.co_filename, 'f1')
    self.assertEqual(co2.co_filename, 'f2')
