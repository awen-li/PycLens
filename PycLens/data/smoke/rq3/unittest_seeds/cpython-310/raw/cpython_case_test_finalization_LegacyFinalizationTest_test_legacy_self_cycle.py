# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_finalization.py
# case: LegacyFinalizationTest_test_legacy_self_cycle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with SimpleBase.test():
        s = LegacySelfCycle()
        ids = [id(s)]
        wr = weakref.ref(s)
        del s
        gc.collect()
        self.assert_del_calls([])
        self.assert_tp_del_calls([])
        self.assert_survivors([])
        self.assert_garbage(ids)
        self.assertIsNot(wr(), None)
        gc.garbage[0].ref = None
    self.assert_garbage([])
    self.assertIs(wr(), None)
