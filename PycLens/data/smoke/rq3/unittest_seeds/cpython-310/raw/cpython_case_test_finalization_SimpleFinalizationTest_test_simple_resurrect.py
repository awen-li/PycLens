# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_finalization.py
# case: SimpleFinalizationTest_test_simple_resurrect

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with SimpleBase.test():
        s = SimpleResurrector()
        ids = [id(s)]
        wr = weakref.ref(s)
        del s
        gc.collect()
        self.assert_del_calls(ids)
        self.assert_survivors(ids)
        self.assertIsNot(wr(), None)
        self.clear_survivors()
        gc.collect()
        self.assert_del_calls(ids)
        self.assert_survivors([])
    self.assertIs(wr(), None)
