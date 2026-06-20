# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCCallbackTests_test_collect_generation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.preclean()
    gc.collect(2)
    for v in self.visit:
        info = v[2]
        self.assertEqual(info['generation'], 2)
