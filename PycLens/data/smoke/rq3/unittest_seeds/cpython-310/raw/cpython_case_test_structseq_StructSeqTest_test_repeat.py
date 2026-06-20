# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_structseq.py
# case: StructSeqTest_test_repeat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t1 = time.gmtime()
    t2 = 3 * t1
    for i in range(len(t1)):
        self.assertEqual(t2[i], t2[i + len(t1)])
        self.assertEqual(t2[i], t2[i + 2 * len(t1)])
