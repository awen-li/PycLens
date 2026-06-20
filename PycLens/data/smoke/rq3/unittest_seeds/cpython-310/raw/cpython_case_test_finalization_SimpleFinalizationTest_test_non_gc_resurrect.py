# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_finalization.py
# case: SimpleFinalizationTest_test_non_gc_resurrect

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with SimpleBase.test():
        s = NonGCResurrector()
        self.assertFalse(gc.is_tracked(s))
        ids = [id(s)]
        del s
        gc.collect()
        self.assert_del_calls(ids)
        self.assert_survivors(ids)
        self.clear_survivors()
        gc.collect()
        self.assert_del_calls(ids * 2)
        self.assert_survivors(ids)
