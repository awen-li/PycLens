# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_structseq.py
# case: StructSeqTest_test_tuple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = time.gmtime()
    self.assertIsInstance(t, tuple)
    astuple = tuple(t)
    self.assertEqual(len(t), len(astuple))
    self.assertEqual(t, astuple)
    for i in range(-len(t), len(t)):
        self.assertEqual(t[i:], astuple[i:])
        for j in range(-len(t), len(t)):
            self.assertEqual(t[i:j], astuple[i:j])
    for j in range(-len(t), len(t)):
        self.assertEqual(t[:j], astuple[:j])
    self.assertRaises(IndexError, t.__getitem__, -len(t) - 1)
    self.assertRaises(IndexError, t.__getitem__, len(t))
    for i in range(-len(t), len(t) - 1):
        self.assertEqual(t[i], astuple[i])
