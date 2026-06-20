# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_structseq.py
# case: StructSeqTest_test_constructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = time.struct_time
    self.assertRaises(TypeError, t)
    self.assertRaises(TypeError, t, None)
    self.assertRaises(TypeError, t, '123')
    self.assertRaises(TypeError, t, '123', dict={})
    self.assertRaises(TypeError, t, '123456789', dict=None)
    s = '123456789'
    self.assertEqual(''.join(t(s)), s)
