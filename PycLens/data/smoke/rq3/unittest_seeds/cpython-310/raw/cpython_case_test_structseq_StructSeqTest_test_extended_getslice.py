# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_structseq.py
# case: StructSeqTest_test_extended_getslice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = time.gmtime()
    L = list(t)
    indices = (0, None, 1, 3, 19, 300, -1, -2, -31, -300)
    for start in indices:
        for stop in indices:
            for step in indices[1:]:
                self.assertEqual(list(t[start:stop:step]), L[start:stop:step])
