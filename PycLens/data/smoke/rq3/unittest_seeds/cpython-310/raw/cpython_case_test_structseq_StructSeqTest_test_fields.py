# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_structseq.py
# case: StructSeqTest_test_fields

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = time.gmtime()
    self.assertEqual(len(t), t.n_sequence_fields)
    self.assertEqual(t.n_unnamed_fields, 0)
    self.assertEqual(t.n_fields, time._STRUCT_TM_ITEMS)
